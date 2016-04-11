## Crunch Benchmarks

PNG optimization benchmarks were executed with Crunch v0.9.0.  They use [the PNG Test Corpus files](http://css-ig.net/images/png-test-corpus.zip) that are maintained by css-ig.net.  A broad analysis of available PNG optimization tools is available [here](http://css-ig.net/png-tools-overview) for additional reference.

In the following table, `Size In` and `Size Out` represent the original and optimized file size in bytes, respectively.  `%Original Size` is the percent of the original file size in bytes represented by the final optimized file size.  A lower value is better.

The `DSSIM` value is a measure of dissimilarity between two PNG images. It uses [the SSIM algorithm](https://ece.uwaterloo.ca/%7Ez70wang/research/ssim/) and is calculated with [the open source dssim tool](https://github.com/pornel/dssim) by [@pornel](https://github.com/pornel).  This is calculated from the optimized file using the original file as a reference.  Interpretation is as follows (from the dssim README):

> The value returned is 1/SSIM-1, where 0 means identical image, and >0 (unbounded) is amount of difference.


| File                | Size In      | Size Out         |  % Original Size   |  DSSIM         |
| :-----------------: | ------------:| ----------------:| :----------------: | :------------: |
| 01-c3-c0.png        |  18623       |  9325            |  50.07%            |  0.00027151    |
| 02-c4-c0.png        |  2794        |  1100            |  39.37%            |  0.00000754    |
| 03-c6-c2.png        |  12771       |  4175            |  32.69%            |  0.00000769    |
| 04-c2-f0-f5.png     |  1539        |  569             |  36.97%            |  0.00000000    |
| 05-c3-c2.png        |  1416        |  751             |  53.04%            |  0.00012144    |
| 06-c6-c3.png        |  12346       |  6809            |  55.15%            |  0.00008878    |
| 07-c4-c3.png        |  15280       |  7167            |  46.90%            |  0.00002324    |
| 08-c0-c3.png        |  15855       |  11836           |  74.65%            |  0.00008729    |
| 09-c3-tronc.png     |  3842        |  2437            |  63.43%            |  0.00005157    |
| 10-c3-t-first.png   |  2893        |  1214            |  41.96%            |  0.00001440    |
| 11-8-to-4bit.png    |  3036        |  1346            |  44.33%            |  0.00000000    |
| 12-4-to-8bit.png    |  11667       |  9875            |  84.64%            |  0.00006822    |
| 13-idat.png         |  7828        |   997            |  12.74%            |  0.00000994    |
| 14-chunks.png       |  2032        |   997            |  49.06%            |  0.00000994    |
| 15-pal-org.png      |  24551       |  16017           |  65.24%            |  0.00016014    |
| 16-pal-org-t.png    |  24795       |  16133           |  65.07%            |  0.00014012    |
| 17-pal-dup.png      |  3032        |  1346            |  44.39%            |  0.00000000    |
| 18-c2-c3-f.png      |  28840       |  12206           |  42.32%            |  0.00017952    |
| 19-c6-c3-f.png      |  31691       |  11829           |  37.33%            |  0.00016088    |
| 20-c6-c4.png        |  34975       |  16717           |  47.80%            |  0.00003876    |
| 21-rgbdata.png      |  49515       |  37759           |  76.26%            |  0.00000000    |
| **Mean**            |     --       |   --             |  **50.64%**        |  --            |


## Crunch Optimization vs. Other Commonly Used Applications

The values in the following table are the percent of the original file size in the resulting image file following optimization with the respective tool.  Lower values are better.

Tests were performed using commands that permit direct comparison to the reference tables in the [PNG Optimization Tools Overview](http://css-ig.net/png-tools-overview) that is maintained by Cédric Louvrier.

#### ImageOptim Tests

ImageOptim v1.6.1 was executed via drag and drop into the GUI application.

#### OptiPNG Tests

`optipng` v0.7.5 was executed with the command:

```
$ optipng -o3 [filepath]
```

#### PNGOUT Tests

`pngout` vSep 20 2015 was executed with the command:

```
$ pngout [filepath]
```

#### PNGCrush Tests

`pngcrush` v1.8.0 was executed with the command:

```
$ pngcrush -brute -blacken -reduce [filepath]
```

Please note that Crunch uses a *lossy* PNG optimization approach that is based upon minimum acceptable image quality whereas the comparison tools are all executed with purely *lossless* PNG optimization.  The selectively lossy approach in Crunch is intentional, explains the file size difference, and should be taken into consideration as you interpret the findings and make decisions about use cases for the tool.


| File                | Crunch        | ImageOptim       |  OptiPNG            |  PNGOUT       | PNGCrush    |
| :-----------------: | :------------:| :---------------:| :----------------: | :------------: | :---------: |
| 01-c3-c0.png        |  50.07%       |  58.70%          |  64.17%            |   83.83%       |  88.35%     |
| 02-c4-c0.png        |  39.37%       |  45.92%          |  48.85%            |   76.77%       |  66.00%     |
| 03-c6-c2.png        |  32.69%       |  62.03%          |  70.56%            |   81.87%       |  70.60%     |
| 04-c2-f0-f5.png     |  36.97%       |  35.61%          |  37.23%            |   83.82%       |  37.17%     |
| 05-c3-c2.png        |  53.04%       |  37.50%          |  78.67%            |   100.00%      |  78.53%     |
| 06-c6-c3.png        |  55.15%       |  61.03%          |  63.67%            |   75.06%       |  80.77%     |
| 07-c4-c3.png        |  46.90%       |  68.63%          |  74.24%            |   79.99%       |  85.62%     |
| 08-c0-c3.png        |  74.65%       |  85.64%          |  88.47%            |   93.52%       |  88.49%     |
| 09-c3-tronc.png     |  63.43%       |  66.74%          |  73.06%            |   67.10%       |  73.19%     |
| 10-c3-t-first.png   |  41.96%       |  76.36%          |  79.47%            |   81.68%       |  79.47%     |
| 11-8-to-4bit.png    |  44.33%       |  44.01%          |  73.62%            |   50.92%       |  57.35%     |
| 12-4-to-8bit.png    |  84.64%       |  82.72%          |  89.23%            |   87.98%       |  89.23%     |
| 13-idat.png         |  12.74%       |  15.24%          |  16.88%            |   15.69%       |  16.88%     |
| 14-chunks.png       |  49.06%       |  58.56%          |  88.93%            |   60.43%       |  87.70%     |
| 15-pal-org.png      |  65.24%       |  90.17%          |  96.51%            |   91.54%       |  95.65%     |
| 16-pal-org-t.png    |  65.07%       |  91.27%          |  97.81%            |   91.49%       |  96.97%     |
| 17-pal-dup.png      |  44.39%       |  44.36%          |  49.80%            |   50.36%       |  57.85%     |
| 18-c2-c3-f.png      |  42.32%       |  61.76%          |  61.24%            |   78.54%       |  83.42%     |
| 19-c6-c3-f.png      |  37.33%       |  56.62%          |  50.11%            |   77.10%       |  79.23%     |
| 20-c6-c4.png        |  47.80%       |  59.95%          |  64.19%            |   78.64%       |  64.31%     |
| 21-rgbdata.png      |  76.26%       |  76.26%          |  88.24%            |   85.78%       |  82.53%     |
| **Mean**            |  **50.64%**   |   **60.91%**     |  **69.28%**        |  **75.81%**    | **74.25%**  |
