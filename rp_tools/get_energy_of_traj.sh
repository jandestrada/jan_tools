#!/usr/bin/bash
grep "FINAL ENERGY" */tc.out | awk '{print $1 "  "  $3}' > trajectory_energy.txt

