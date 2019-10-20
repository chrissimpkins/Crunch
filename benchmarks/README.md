## Crunch Benchmarks

This directory includes reference PNG files from http://www.schaik.com/pngsuite/ for benchmarking the Crunch PNG optimization approach. The  image files in this directory are distributed under the [PngSuite.LICENSE](PngSuite.LICENSE).

Benchmarks are performed against all PNG image files released in the http://www.schaik.com/pngsuite/PngSuite-2017jul19.tgz archive *except* the [reference corrupted files](http://www.schaik.com/pngsuite/#corrupted).


## How to Execute Benchmarks Locally

Clone this repository, build the dependency tools, install the `crunch` executable, and run benchmarks with the following set of commands:

```
$ git clone https://github.com/chrissimpkins/Crunch.git
$ make build-dependencies
$ make install-executable
$ make benchmark
```

The benchmark output is displayed in your terminal.
