# python-turnitin

Clone Project
`git clone git@github.com:enisbe1/python-turnitin.git` using SSH
`git clone https://github.com/enisbe1/python-turnitin.git` using HTTP

Move to develop branch
`git checkout develop`

Get all the datas
`git pull origin develop`
All ready for developing on your local personal computer

Now assume that you want to add something new to the code
First we create a branch based on what we want to add if new feature or a fix
The branch names are prefered to follow the structure `feat/feature-name`, `fix/fix-name`
After creating the new branch we start to code, when finished
use
`git add .` to add all files in the stage
`git commit -m "Message typed here"` to commit the changes, message should be short and meaningfull
And in the end we use
`git push origin branch-name` to push the changes to the repository
We create a pull request with the branch develop which should be merged after being reviewed by colleagues
