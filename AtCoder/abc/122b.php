<?php

$s = trim(fgets(STDIN));
$count = [0];

$replace = preg_replace('/[^ACGT]/',',',$s);
$matchs = array_filter(explode(',',$replace));

foreach ($matchs as $m) {
    $count[] = strlen($m);
}

print(max($count) . "\n");