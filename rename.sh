# take 1 parameter, a directory name
# rename all files in the directory to have the prefix like "lesson9_"

# check if the user has provided a directory name
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# check if the directory exists
if [ ! -d $1 ]; then
    echo "Directory $1 does not exist"
    exit 2
fi

# check if the directory is empty
if [ ! "$(ls -A $1)" ]; then
    echo "Directory $1 is empty"
    exit 3
fi

# rename all files in the directory
for file in $1/*; do
    mv $file $1/$1_$(basename $file)
done

echo "All files in $1 have been renamed"