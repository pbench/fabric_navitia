# Extra Tools used to deploy

## retreive_debian_packages_from_github 

**Github Actions** is capable of creating **artifacts** from a specific job.<br>
Artifacts can be downloaded via the github API.<br>
We want to retrieve the **last Navitia Debian packages** (in *success*) compressed in a zip file.<br>
To perform it, the script does:
- Find the related workflow (id)
- Retrieve the last run (in success) of the workflow
- Dowmload the associated artifacts (in a zip file)

script type : python 2

### How to install 

```
# Create your own virtual env
# and install dependencies
pip install -r requirements.txt
```

### How to run it 

```
# Help
pythonn2.7 retreive_debian_packages_from_github.py -h

# Example
pythonn2.7 retreive_debian_packages_from_github.py -u {GithubUser} -t {GithubToken} -w {workflow name} -a {artifacts.zip} -o {output_path}
```


