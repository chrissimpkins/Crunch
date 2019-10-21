## Crunch Benchmarks

This directory includes reference PNG files from http://www.schaik.com/pngsuite/ for benchmarking Crunch PNG optimization. The  image files in this directory are distributed under the [PngSuite.LICENSE](PngSuite.LICENSE).

Benchmarks are performed against all PNG image files released in the http://www.schaik.com/pngsuite/PngSuite-2017jul19.tgz archive *except* the [reference corrupted files](http://www.schaik.com/pngsuite/#corrupted).

The [results of continuous benchmark testing are available on Travis CI in the "Benchmarks" build](https://travis-ci.org/chrissimpkins/Crunch).

## How to Execute Benchmarks Locally

Clone this repository, build the dependency tools, install the `crunch` executable, and run benchmarks with the following set of commands:

```
$ git clone https://github.com/chrissimpkins/Crunch.git
$ make build-dependencies
$ make install-executable
$ make benchmark
```

The benchmark output is displayed in your terminal.

The optimized image files remain in the benchmarks directory after execution for your review.  To clean the optimized files, use the following command:

```
$ make clean
```

## How to Benchmark With Other Image Sets

The Python 3 [`bench.py` script](bench.py) in this directory is portable.  Download the script, drop it into the directory with your image files, execute `crunch` on all images in the directory, and execute the benchmark script with:

```
$ python3 bench.py
```

**Note**: Do not include extraneous *.png files in the directory that you use for benchmarking and optimize all files that are included in the directory before you execute the script.
