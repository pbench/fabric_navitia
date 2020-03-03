# Extra Tools used to deploy

## retreive_debian_packages_from_github 

Github Actions is capable to create artifacts from a specific job.
Artifacts can be downloaded via the github API
We want to reteive the last Navitia Debian packages (in success) compressed in a zip file.
To perform it, the script does:
- Find the concerned workflow (id)
- Retreive the last run (in success) of the workflow
- Dowmload the associated artifacts (in a zip file)

script type : python 2

### How to install 

```
# Create your own virtual env
pip install -r requirements.txt
```

### How to run it 

```
# Help
pythonn2.7 retreive_debian_packages_from_github.py -h

# example
pythonn2.7 retreive_debian_packages_from_github.py -u {GithubUser} -t {GithubToken} -w {workflow name} -a {artifacts.zip} -o {output_path}
```


