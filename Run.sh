#dir= $(cd $(dirname "$0"); pwd)
dir=`dirname $0`
cd $dir

python `pwd`/main.py 80
