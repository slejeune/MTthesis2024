
# All the different prompt options to run finetuning for
PROMPTS=("t-enc" "t-dec" "s-enc-t-enc" "s-enc-t-dec")

ALPHA=0.1
DATA=~/MThesis/CrossConST-LLM/NLLB-flores200_dev.high_low.json

for ((n = 0 ; n < ${#PROMPTS[@]} ; n++)); do

	CKPT=ALMA-13B-Pretrain-PEFT-MT-${PROMPTS[n]}-alpha01-high-low

	torchrun --nnodes 1 --nproc_per_node 2 examples/finetuning.py --dataset translation_dataset --prompt_type ${PROMPTS[n]} \
    	--data_path ${DATA} \
    	--model_name haoranxu/ALMA-13B-Pretrain \
    	--num_epochs 1 --batch_size_training 4 \
    	--lr 1e-4 --gradient_accumulation_steps 8 \
    	--use_peft --peft_method lora --output_dir ${CKPT} \
    	--enable_fsdp --use_fast_kernels \
    	--xconst_alpha ${ALPHA} \
	--pure_bf16 \
		2>&1 | tee -a logs/EXP.txt

done