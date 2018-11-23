# usage 
go to your git repository
buildcomparator.py path/to/buildartifact.jar /path/to/buildartifact.jar
where the first argument specifies the path to where maven produces its build artifact and the second the path to the artifact to compare against

## workings

list all branches
check out the first one
    run maven package
    compare against the reference artifact
    output a similarity score
    go down in history and repeat
do the same for other branches
