# Test Sequencer

Run the main executable

```shell
cd path/to/test-sequencer
python .
```

The output should look like:

```
aclr called with (4g, 1, 4)
aclr called with (5g, 1, 4)
aclr called with (6g, 1, 4)
aclr called with (all-the-gs, 1, 4)
aclr called with (4g, 2, 4)
aclr called with (5g, 2, 4)
aclr called with (6g, 2, 4)
aclr called with (all-the-gs, 2, 4)
...
ac_power called with 100 V / 50 Hz AC
ac_power called with 110 V / 50 Hz AC
ac_power called with 120 V / 50 Hz AC
ac_power called with 127 V / 50 Hz AC
...
```

Two files, `ac_power.csv` and `aclr.csv`, are generated.
