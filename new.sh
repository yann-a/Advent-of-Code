DAY=${1:-"$(date +'%d')"}
YEAR=${2:-"$(date +'%Y')"}

DAY_NOPAD=${DAY##0}

if test -e $YEAR
then
    cd $YEAR
    if test -e $DAY
    then
        echo "day $DAY already exists"
    else
        mkdir $DAY
        cp ../template.py $DAY/main.py
        cd $DAY
        sed -i -e "s/YEAR/$YEAR/g" main.py
        sed -i -e "s/DAY/$DAY_NOPAD/g" main.py
        code .. -g main.py:9:5
        firefox https://adventofcode.com/$YEAR/day/$DAY_NOPAD
    fi
else
    echo "year $YEAR doesn't exist"
fi
