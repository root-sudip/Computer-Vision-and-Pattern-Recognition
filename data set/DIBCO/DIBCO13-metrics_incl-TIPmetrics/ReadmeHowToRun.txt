DIBCO 2013 Evaluation Tool

4 Inputs, filenames of:
I.1 GT image
I.2 Binarized image for evaluation
I.3 "Recall Weights"** .dat file
I.4 "Precision Weights"** .dat file

8 Outputs:
O.1 F-Measure
O.2 pseudo F-Measure (Fps)**
O.3 PSNR
O.4 DRD***
O.5 Recall
O.6 Precision
O.7 pseudo-Recall (Rps)**
O.8 pseudo-Precision (Pps)**

The outputs are tab delimited with a newline at the end.

*Notice that for I.3 and I.4 a different executable program
is required to generate the .dat files containing the "Recall/Precision weights"
(http://users.iit.demokritos.gr/~kntir/TIP_exe/).

**K. Ntirogiannis, B. Gatos and I. Pratikakis,
"Performance Evaluation Methodology for Historical Document Image Binarization",
IEEE Trans. Image Proc., vol.22, no.2, pp. 595-609, Feb. 2013.

***H.Lu, A.C. Kot and Y.Q. Shi,
"Distance Reciprocal Distortion Measure for Binary Document Images",
IEEE Sigal Proc. Lett., vol.11, no.2, pp. 228-231, Feb. 2004.

Example Run:
C:\EvalDIBCO2013\Tool>DIBCO13_metrics.exe PR_GT.tiff PR_bin.bmp PR_RWeights.dat PR_PWeights.dat
93.598747       97.686342       15.816293       1.868077        90.460729
96.962300       99.446358       95.987541


(*)CAUTION: When providing the .dat files,
always provide the "Recall weights" .dat file first
and afterwards the "Precision weights" .dat file.