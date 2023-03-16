```
blenderpoc run examples/datasets/bop_challenge/main_<bop_dataset_name>_<random/upright>.py 
               <path_to_bop_data> 
               resources/cctextures 
               examples/datasets/bop_challenge/output
               --num_scenes=2000
``` 

```
train:

blenderproc run examples/datasets/bop_challenge/main_lm_upright.py "D:\bop_toolkit\data" "D:\bop_toolkit\blenderproc_textures" "D:\bop_toolkit\data\251_lm_251" --num_scenes=40 --obj_ids '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16'
python C:\Users\grandid\source\repos\bop_toolkit\scripts\calc_gt_masks.py
python C:\Users\grandid\source\repos\bop_toolkit\scripts\calc_gt_info.py

``` 
```
val:

blenderproc run examples/datasets/bop_challenge/main_lm_upright.py "D:\bop_toolkit\data" "D:\bop_toolkit\blenderproc_textures" "D:\bop_toolkit\data\lm\blenderproc" --num_scenes=1 --obj_ids '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16' --val
python C:\Users\grandid\source\repos\bop_toolkit\scripts\calc_gt_masks.py --val
python C:\Users\grandid\source\repos\bop_toolkit\scripts\calc_gt_info.py --val
``` 