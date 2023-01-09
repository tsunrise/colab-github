# Access GitHub Private Repo in Google Colab
<a target="_blank" href="https://colab.research.google.com/github/tsunrise/colab-github/blob/main/Access_GitHub_Private_Repo.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

Authenticate with GitHub in Google Colab to access private repo.

## Steps
- Run the following code inside the colab notebook.
```python
!wget -q https://raw.githubusercontent.com/tsunrise/colab-github/main/colab_github.py
import colab_github
colab_github.github_auth(persistent_key=True)
```
Note that by setting `persistent_key` to true, you will be asked to connect to Google Drive, so this script will store private key inside your `.colab-github` folder of your Google Drive. Doing so, you only need to upload your private key to Github once.

- You will see outputs like:
```
Please go to https://github.com/settings/ssh/new to upload the following key:  
ssh-ed25519 xxxxxxx/xxxxxxxxxxxxxxxxxxxx root@xxxxxxxxxxxxxxxx
```
Upload this public key to either your [SSH settings](https://github.com/settings/ssh/new), or your repo's Deploy Keys.

- Use **SSH** method to clone your private repo. Inside the notebook, you can run
```python
!git clone git@github.com:<your_username>/<your_private_repo>.git
```

