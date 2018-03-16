/usr/local/openmpi-2.0.1/bin/mpirun -np 8 \
/data/nfs_share2/public/zhenghonghui/rocs/build/tools/caffe train \
--solver resnet50_solver.prototxt \
--snapshot snapshots/resnet50_s3_iter_1922000.solverstate \
--gpu all
