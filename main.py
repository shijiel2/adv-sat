import socket
from subprocess import call
from notification import NOTIFIER

CIFAR10_TRAIN_COMMAND = "python train.py --dataset cifar10 -n 100 --epoch_adv 0 --gpu 0 --arch wide --sgd --sink --sink_eps 1 -f wide_resnet_sink_cifar10.ckpt -c _wide_resnet_sink_cifar10 --resume"
CIFAR10_TEST_COMMAND = "python test_adv.py --arch wide --dataset cifar10 --eps 8 -a PGD -f wide_resnet_sink_cifar10.ckpt -l 8 --gpu 0"

CIFAR100_TRAIN_COMMAND = "python train.py --dataset cifar100 -n 100 --epoch_adv 0 --gpu 0 --arch wide --sgd --sink --sink_eps 1 -f wide_resnet_sink_cifar100.ckpt -c _wide_resnet_sink_cifar100 --resume"
CIFAR100_TEST_COMMAND = "python test_adv.py --arch wide --dataset cifar100 --eps 8 -a PGD -f wide_resnet_sink_cifar100.ckpt -l 8 --gpu 0"

cmds = [CIFAR100_TRAIN_COMMAND, CIFAR100_TEST_COMMAND]
for cmd in cmds:
    proc = call(cmd.split())

NOTIFIER.notify(socket.gethostname(), 'AML_OT_baseline_adv_sat Finished :)')