#!/bin/bash
set -e

echo "Testing C files..."
for i in $(ls -1 **/*.c); do
    echo "    Compiling $i - gcc $i -lm -std=c11"
    gcc $i -lm -std=c11
    echo "    Running $i - ./a.out > /dev/null"
    ./a.out > /dev/null
    rm -f a.out
    echo ""
done

echo ""
echo "Testing C++ files..."
for i in $(ls -1 **/*.cpp); do
    echo "    Compiling $i - g++ $i -lm -pthread -std=c++11"
    g++ $i -lm -pthread -std=c++11
    echo "    Running $i - ./a.out > /dev/null"
    ./a.out > /dev/null
    rm -f a.out
    echo ""
done

echo ""
echo "Testing Java files..."
for i in $(ls -1 **/*.java); do
    echo "    Compiling $i - javac -Werror -Xlint:all $i -d ."
    javac -Werror -Xlint:all $i -d .
    filename="${i##*/}"
    classname="${filename%.*}"
    echo "    Running $i - java $classname > /dev/null"
    java $classname > /dev/null
    echo ""
done
rm -f *.class

echo "Testing Python files..."
for i in $(ls -1 **/*.py); do
    echo "    Running $i - python2 $i > /dev/null"
    python2 $i > /dev/null
    echo "    Running $i - python3 $i > /dev/null"
    python3 $i > /dev/null
    echo ""
done

echo ""
echo "Running Go files..."
for i in $(ls -1 **/*.go); do
    echo "    Running $i - go run $i > /dev/null"
    go run $i > /dev/null
    echo ""
done

echo ""
echo "Running JavaScript files..."
for i in $(ls -1 **/*.js); do
    echo "    Running $i - node --use-strict --harmony $i > /dev/null"
    node --use-strict --harmony $i > /dev/null
    echo ""
done

echo ""
echo "Running C# files..."
for i in $(ls -1 **/*.cs); do
    echo "    Compiling $i - mcs $i"
    mcs $i
    excname="${i%.*}".exe
    echo "    Running $i - mono $excname > /dev/null"
    mono $excname > /dev/null
    echo ""
done
