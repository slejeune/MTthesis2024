
ALPHA=0
PROMPT=gpt-mt

CKPT=ALMA-13B-Pretrain-PEFT-MT-${PROMPT}-alpha0-low-low-NONCAUSAL
DATA=~/MThesis/CrossConST-LLM/NLLB-flores200_dev.low_low.json

torchrun --nnodes 1 --nproc_per_node 3 examples/finetuning.py --dataset translation_dataset --prompt_type ${PROMPT} \
    	--data_path ${DATA} \
    	--model_name haoranxu/ALMA-13B-Pretrain \
    	--num_epochs 1 --batch_size_training 4 \
    	--lr 1e-4 --gradient_accumulation_steps 8 \
    	--use_peft --peft_method lora --output_dir ${CKPT} \
    	--enable_fsdp --use_fast_kernels \
    	--xconst_alpha ${ALPHA} \
	--pure_bf16 \
		2>&1 | tee -a logs/EXP.txt

CKPT=ALMA-13B-Pretrain-PEFT-MT-${PROMPT}-alpha0-high-low-NONCAUSAL
DATA=~/MThesis/CrossConST-LLM/NLLB-flores200_dev.high_low.json

torchrun --nnodes 1 --nproc_per_node 3 examples/finetuning.py --dataset translation_dataset --prompt_type ${PROMPT} \
    	--data_path ${DATA} \
    	--model_name haoranxu/ALMA-13B-Pretrain \
    	--num_epochs 1 --batch_size_training 4 \
    	--lr 1e-4 --gradient_accumulation_steps 8 \
    	--use_peft --peft_method lora --output_dir ${CKPT} \
    	--enable_fsdp --use_fast_kernels \
    	--xconst_alpha ${ALPHA} \
	--pure_bf16 \
		2>&1 | tee -a logs/EXP.txt

CKPT=ALMA-13B-Pretrain-PEFT-MT-${PROMPT}-alpha0-high-high-NONCAUSAL
DATA=~/MThesis/CrossConST-LLM/NLLB-flores200_dev.fr_nl_jp_tg.json

torchrun --nnodes 1 --nproc_per_node 3 examples/finetuning.py --dataset translation_dataset --prompt_type ${PROMPT} \
    	--data_path ${DATA} \
    	--model_name haoranxu/ALMA-13B-Pretrain \
    	--num_epochs 1 --batch_size_training 4 \
    	--lr 1e-4 --gradient_accumulation_steps 8 \
    	--use_peft --peft_method lora --output_dir ${CKPT} \
    	--enable_fsdp --use_fast_kernels \
    	--xconst_alpha ${ALPHA} \
	--pure_bf16 \
		2>&1 | tee -a logs/EXP.txt


