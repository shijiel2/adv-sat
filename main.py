import socket
from subprocess import call
from notification import NOTIFIER

CIFAR10_TRAIN_COMMAND = "python train.py --dataset cifar10 -n 60 --epoch_adv 0 --gpu 0 --arch wide --sgd --sink --sink_eps 1 -f wide_resnet_sink_cifar10.ckpt -c _wide_resnet_sink_cifar10"
CIFAR10_TEST_COMMAND = "python test_adv.py --arch wide --dataset cifar10 --eps 8 -a PGD -f wide_resnet_sink_cifar10.ckpt -l 8 --gpu 0"

cmd = CIFAR10_TRAIN_COMMAND
proc = call(cmd.split())

NOTIFIER.notify(socket.gethostname(), 'AML_OT_baseline_adv_sat Finished :)')