# How to git+github

In the readme I describe briefly how to interact with this repo:
  * Fork this repository.
  * Clone your fork to your PC.
  * Create your (group) folder and add any material you would like.
  * Commit your changes to git.
  * Push your changes to your fork.
  * Create a pull request, requesting to pull the changes from your fork into this repository.

In this document I will go through the steps 1-by-1. 

## 1. Fork this repository
To begin with the repository sits in _my_ github account, and the url is _https://github.com/Kristianuruplarsen/sdseml_online_exercises_. Our first step will be to copy all of these files to _your_ account. To do this, navigate to my repo and click on _fork_.

![fork it](/TA_EXAMPLE_FOLDER/FIGURES/hit_fork.PNG)

You should see a screen pop up, informing you that the files are being copied. 

## 2. Clone your fork to your PC
Now you have a personal version of my repository, but it lives on github. We need to download all of these files to your computer for you to work with them. To do this open **Github Desktop**. Click on _current repository_ and on _add_. 

![clone it](/TA_EXAMPLE_FOLDER/FIGURES/clone.PNG)

Find your repository in the list, and hit _clone_. (note that I get a warning because i already have a version of the repository on my PC)

![clone it 2](/TA_EXAMPLE_FOLDER/FIGURES/clone2.PNG)

## 3. Create your group folder and add any changed you would like
Complete the exercises.

## 4. Commit your changes to git
Git does not track every file on your pc. Only the ones that you have committed to the repository. Thus before you can convince git to push your changes back to github.com you need to commit them. To do this, open Github Desktop again (and open your *sds_online_exercises* repo). You should now see the changes you have made listed under _changes_. Write a summary message, that describes the work you are committing, and hit _commit to master_.

![commit](/TA_EXAMPLE_FOLDER/FIGURES/commit.PNG)

After hitting commit, you should see that the number of changes (since last commit) is reduced to 0. 

## 5. Push your changes
Now your work is done and committed locally on your pc. To get the changes onto github, you need to _push_ them. This is as easy as hitting _push origin_ in Github Desktop. (Note, if you are collaborating with someone else, you need to pull all the most recent changes from github before you can push. It all happens on the same button).

![push](/TA_EXAMPLE_FOLDER/FIGURES/push.PNG)

## 6. Create a pull request
Now your files are online, but they are located in _your fork_, not in my _base repository_. To further push your changes into my repo, you need to create a pull request. (Note, because I have control over _my repo_, you cannot push to it. Instead you can request that I pull from your repo). 

To do this, open your repo on github (url: _https://github.com/YOUR_USERNAME/sdseml_online_exercises_). You should see the files you just committed and pushed. Click on _pull requests_

![pull](/TA_EXAMPLE_FOLDER/FIGURES/pull.PNG)

Then hit _new pull request_

![pull 2](/TA_EXAMPLE_FOLDER/FIGURES/pull2.PNG)

Finally hit _create pull request_ and wait. 


## Conclusion
This seems like a lot of work just to upload some files. For some purposes it is, but in situations where many people collaborate on the same project (e.g. in a company) it is super helpful to divide the merging process into multiple steps. This makes it easier to spot mistakes, while avoiding the *_version_24_somerandomperson.py* curse.
