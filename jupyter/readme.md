# make sure your environment contains the jupyter package
>> conda list | grep jupyter

# and any packages required by the notebook
conda list | grep <package name>

# start the jupyter server:
>> jupyter notebook --notebook-dir "C:\dev\code\scipy-2016-sklearn"