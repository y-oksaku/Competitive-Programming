<?php
$n = (int) trim(fgets(STDIN));

$count = [0,0,0,0,0];
$count[0] = (int) trim(fgets(STDIN));
$count[1] = (int) trim(fgets(STDIN));
$count[2] = (int) trim(fgets(STDIN));
$count[3] = (int) trim(fgets(STDIN));
$count[4] = (int) trim(fgets(STDIN));

$min = min($count);

$time = ceil($n / $min);

echo (int)($time + 4) . "\n";