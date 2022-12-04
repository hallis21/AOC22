$res = 0
 #
$res_table = @{A=@{X=3;Y=4;Z=8};B=@{X=1;Y=5;Z=9};C=@{X=2;Y=6;Z=7}}
 #
[ForEach($x in Get-Content -Path 'inp.txt') {$res = $res + $res_table[$x[0]][$x[2]]}]
 #
Write-Host $res #