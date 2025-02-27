python3 core/test_xportrait.py \
--model_config config/cldm_v15_appearance_pose_local_mm.yaml \
--output_dir outputs \
# --resume_dir checkpoint/model_state-415001.th \
--seed 999 \
--uc_scale 5 \
--source_image assets/source_image.png \
--driving_video assets/driving_video.mp4 \
--best_frame 36 \
--out_frames -1 \
--num_mix 4 \
--ddim_steps 30 \