Set-Location -Path "..\src"

$env:CUDA_VISIBLE_DEVICES = "0"

$tta_algo = 'Ramen'
$tta_mode = 'mixed'

$datasets = @('CIFAR10C', 'CIFAR100C', 'ImageNetC5K', 'DomainNet')
$models = @('clip_vitbase32', 'clip_vitbase16', 'clip_vitlarge14', 'clip_vitbase32')
$batch_sizes = @(100, 100, 50, 100)

for ($i = 0; $i -lt 4; $i++) {
    $dataset = $datasets[$i]
    $model = $models[$i]
    $batch_size = $batch_sizes[$i]
    $save_to = "../log/${dataset}_${tta_mode}/${tta_algo}.csv"

    Write-Host "Running: $dataset with model $model"
    python main.py --dataset $dataset --model $model --tta_algo $tta_algo --tta_mode $tta_mode --cuda --batch_size $batch_size --save_to $save_to
}
