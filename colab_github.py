def github_auth(persistent_key: bool):
  """
  Authenticate with GitHub to access private repo. This function will 
  detect if there is `id_ed25519` key SSH profile. If not, it will create
  one. 
  - `persistent_key`: Store private key in Google Drive.
  """
  import os

  os.system("mkdir -p ~/.ssh")

  if persistent_key:
    from google.colab import drive
    drive.mount('/content/drive/')
    private_key_dir = "/content/drive/MyDrive/.colab-github"
    os.system(f"mkdir -p {private_key_dir}")
  else:
    private_key_dir = "~/.ssh"

  private_key_path = private_key_dir + "/id_ed25519"
  public_key_path = private_key_path + ".pub"

  if not os.path.exists(os.path.expanduser(private_key_path)):
    fresh_key = True
    os.system(f"ssh-keygen -t ed25519 -f {private_key_path} -N ''")
  else:
    fresh_key = False

  if persistent_key:
    os.system("rm -f ~/.ssh/id_ed25519")
    os.system("rm -f ~/.ssh/id_ed25519.pub")
    os.system(f"cp -s {private_key_path} ~/.ssh/id_ed25519")
    os.system(f"cp -s {public_key_path} ~/.ssh/id_ed25519.pub")

  with open(os.path.expanduser(public_key_path), "r") as f:
    public_key = f.read()
    if fresh_key:
      print("Please go to https://github.com/settings/ssh/new to upload the following key: ")
    else:
      print("Looks that a private key is already created. If you have already push it to github, no action required."
      "\n Otherwise, Please go to https://github.com/settings/ssh/new to upload the following key: ")

    print(public_key)

  # add github to known hosts (you may hardcode it to prevent MITM attacks)
  os.system("ssh-keyscan -t ed25519 github.com >> ~/.ssh/known_hosts")

  os.system("chmod go-rwx ~/.ssh/id_ed25519")

  print("Please use SSH method to clone repo.")
