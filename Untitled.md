```
➜ bazel run //wayve/ai/si:deploy -- --session_path /mnt/remote/azure_session_dir/Parking/parking/session_2026_01_28_20_56_18_si_parking_bc_train_wfm_october_2025_pudo_7_17.01_october_wfm_bc --suffix __test --enable_parking --with_temporal_caching true --upload --dilc_on
INFO: Invocation ID: 953f36c5-2c60-433d-afb7-c7ba4a37109e
WARNING: /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/external/com_github_grpc_grpc/src/compiler/BUILD:87:18: target 'grpc_cpp_plugin' is both a rule and a file; please choose another name for the rule
WARNING: /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/external/com_github_grpc_grpc/src/compiler/BUILD:93:18: target 'grpc_csharp_plugin' is both a rule and a file; please choose another name for the rule
WARNING: /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/external/com_github_grpc_grpc/src/compiler/BUILD:99:18: target 'grpc_node_plugin' is both a rule and a file; please choose another name for the rule
WARNING: /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/external/com_github_grpc_grpc/src/compiler/BUILD:105:18: target 'grpc_objective_c_plugin' is both a rule and a file; please choose another name for the rule
WARNING: /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/external/com_github_grpc_grpc/src/compiler/BUILD:111:18: target 'grpc_php_plugin' is both a rule and a file; please choose another name for the rule
WARNING: /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/external/com_github_grpc_grpc/src/compiler/BUILD:117:18: target 'grpc_python_plugin' is both a rule and a file; please choose another name for the rule
WARNING: /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/external/com_github_grpc_grpc/src/compiler/BUILD:123:18: target 'grpc_ruby_plugin' is both a rule and a file; please choose another name for the rule
INFO: Analyzed target //wayve/ai/si:deploy (1723 packages loaded, 154909 targets configured).
INFO: Found 1 target...
Target //wayve/ai/si:deploy up-to-date:
  bzl-build/bin/wayve/ai/si/deploy
INFO: Elapsed time: 8.748s, Critical Path: 0.98s
INFO: 1 process: 1 internal.
INFO: Build completed successfully, 1 total action
INFO: Running command line: bzl-build/bin/wayve/ai/si/deploy --session_path /mnt/remote/azure_session_dir/Parking/parking/session_2026_01_28_20_56_18_si_parking_bc_train_wfm_october_2025_pudo_7_17.01_october_wfm_bc --suffix __test --enable_parking --with_temporal_caching true --upload --dilc_on
INFO     09:24:27,003 azure.identity._credentials.environment No environment configuration found.
WARNING  09:24:27,003 services.common.datadog_client datadog_missing_environment_setup api_key_present=True, app_key_present=False, statsd_host_present=False
INFO     09:24:56,003 weightwatcher Using Scipy for SVD
INFO     09:24:56,003 weightwatcher Torch CUDA available, using torch_wrapper
INFO     09:24:56,003 weightwatcher Using EPSILON = 6e-05
INFO     09:24:56,003 weightwatcher Using EVALS_THRESH = 0.0001


            [Deploy Script Configuration]
            Session path:           /mnt/remote/azure_session_dir/Parking/parking/session_2026_01_28_20_56_18_si_parking_bc_train_wfm_october_2025_pudo_7_17.01_october_wfm_bc
            Output directory:       Not specified
            Step:                   Latest
            Suffix:                 __test
            Upload to console:      True
            Export to ONNX:         False
            Temporal caching:       True
            Speed limit clamp:      Same as trained model
            Behavior control:       Default
            Interface version:      dmi
            Vehicle model:          None
            Deployment country:     Auto-infer from GPS
            Use prototype input:    None
            DILC enabled:           True
            Dtype override:         Same as trained model
            Autocast dtype:         float16
            Speed sign output:      Same as trained model
            Road speed limit:       False
            Road with set speed:    False
            Supported platforms:    gen1, gen2
            Spoofed speed signs:    False
            Disable averager:       False
            ODD output enabled:     Same as trained model
            Backend optimisations:  NVIDIA optimisations
            Enable parking:         True

        
ERROR    09:25:01,003 ..lib.session git_hash_mismatch message=

  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  Currently running code is at a different git commit to when the session directory was created. Restoring training from this point may cause problems.
  This is fully allowed for now, but may cause severe regression guarantee issues in the future.
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

WARNING  09:25:03,003 .configs.versioning.common config_migration message=config_version not found in config, setting to 0, but migrations may not be applied correctly
INFO     09:25:06,003 ..zoo.st.checkpoints load_state_dict message=Checkpoint azure://wayveprodmlexperiments/training-session-store/WayveFoundationModel/wfm_yolo/session_2025_08_19_11_21_08_yolo_ablations_st-16-heads/checkpoints/model-checkpoint-001000000.ckpt
INFO     09:25:06,003 ..lib.checkpoint get_checkpoint_path message=Checkpoint azure://wayveprodmlexperiments/training-session-store/WayveFoundationModel/wfm_yolo/session_2025_08_19_11_21_08_yolo_ablations_st-16-heads/checkpoints/model-checkpoint-001000000.ckpt already exists in cache at /workspace/.cache/ai_lib_cache/models/wayveprodmlexperiments/training-session-store/WayveFoundationModel/wfm_yolo/session_2025_08_19_11_21_08_yolo_ablations_st-16-heads/checkpoints/model-checkpoint-001000000.ckpt
INFO     09:25:11,003 ..zoo.st.checkpoints load_state_dict message=Missing key adaptors.waypoints.dropout.dropout_token, adding default value for backward compatibility
WARNING  09:25:11,003 ..zoo.st.input_adaptors.speed_limit continuous_speed_limit_adaptor message=Missing freqs buffer in checkpoint, setting to initialized value for backward compatibility
WARNING  09:25:11,003 ..zoo.st.input_adaptors.speed_limit continuous_speed_limit_adaptor message=Missing max_val buffer in checkpoint, setting to initialized value for backward compatibility
WARNING  09:25:11,003 ..zoo.st.input_adaptors.speed_limit continuous_speed_limit_adaptor message=Missing norm buffer in checkpoint, setting to initialized value for backward compatibility
WARNING  09:25:11,003 ..zoo.st.input_adaptors.pose pose_adaptor message=Missing rotation_matrix buffer in checkpoint, setting to initialized value for backward compatibility
WARNING  09:25:11,003 ..zoo.st.input_adaptors.temporal continuous_time_encoding message=Missing max_t buffer in checkpoint, setting to initialized value for backward compatibility
WARNING  09:25:11,003 ..zoo.st.input_adaptors.temporal continuous_time_encoding message=Missing w buffer in checkpoint, setting to initialized value for backward compatibility
INFO     09:25:11,003 ..compression.pruning.pruning init pruning_enabled=False, total_param_size=0, pruning_ratio=1.0, desired_total_param_size=0.0
INFO     09:25:11,003 ..lib.checkpoint get_checkpoint_path message=Checkpoint https://wayveprodmlexperiments.blob.core.windows.net/training-session-store/Parking/parking/session_2026_01_28_20_56_18_si_parking_bc_train_wfm_october_2025_pudo_7_17.01_october_wfm_bc/checkpoints/model-checkpoint-000100000.ckpt already exists in cache at /workspace/.cache/ai_lib_cache/models/wayveprodmlexperiments/training-session-store/Parking/parking/session_2026_01_28_20_56_18_si_parking_bc_train_wfm_october_2025_pudo_7_17.01_october_wfm_bc/checkpoints/model-checkpoint-000100000.ckpt
WARNING  09:25:14,003 __main__ checkpoint_load_non_strict message=Loaded checkpoint with strict=False; some keys did not match., missing_keys=[], unexpected_keys=['model.input_adaptor.adaptors.gear_direction.min_val', 'model.input_adaptor.adaptors.gear_direction.max_val', 'model.input_adaptor.adaptors.gear_direction.dropout.dropout_token', 'model.input_adaptor.adaptors.gear_direction.embedding.weight'], missing_count=0, unexpected_count=4
INFO     09:25:15,003 .models.deployment enable_temporal_caching parent_model=MIMOSTTransformer, changed_modules=['VideoSTAdaptor']
INFO     09:25:15,003 .models.deployment deployment_wrapper wrapper_impl_class=<class 'wayve.ai.zoo.deployment.deployment_wrapper.ParkingDeploymentWrapperImpl'>, wrapper_kwargs={'deployment_vehicle_model_override': None, 'max_tick_driving_plan': 0, 'deployment_country': None, 'dilc_on': True, 'deployment_driving_controls_keys': (0, 1, 3)}
INFO     09:25:30,003 ..lib.deploy_decorators prune_model status=start, num_parameters=587882500, model_size_bytes=2351056857
INFO     09:25:30,003 ..lib.deploy_decorators prune_model status=success, duration_ms=6.0, num_parameters=587882500, model_size_bytes=2351056857
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────── Traceback (most recent call last) ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/WayveCode/wayve/ai/si/deploy.py:673 in <module>                                                                                                 │
│                                                                                                                                                                                                                                                                              │
│ ❱ 673 │   deploy(                                                                                                                                                                                                                                                            │
│                                                                                                                                                                                                                                                                              │
│ /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/WayveCode/wayve/ai/si/deploy.py:573 in deploy                                                                                                   │
│                                                                                                                                                                                                                                                                              │
│ ❱ 573 │   compile_and_save_model(                                                                                                                                                                                                                                            │
│                                                                                                                                                                                                                                                                              │
│ /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/pip-core_lightning_utilities/site-packages/lightning_utilities/core/rank_zero.py:41 in wrapped_fn                                               │
│                                                                                                                                                                                                                                                                              │
│ ❱  41 │   │   │   return fn(*args, **kwargs)                                                                                                                                                                                                                                 │
│                                                                                                                                                                                                                                                                              │
│ /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/WayveCode/wayve/ai/lib/deploy.py:296 in compile_and_save_model                                                                                  │
│                                                                                                                                                                                                                                                                              │
│ ❱ 296 │   compiled_model, deployment_config = compile_model(module, deployment_config, jit_fre                                                                                                                                                                               │
│                                                                                                                                                                                                                                                                              │
│ /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/pip-core_lightning_utilities/site-packages/lightning_utilities/core/rank_zero.py:41 in wrapped_fn                                               │
│                                                                                                                                                                                                                                                                              │
│ ❱  41 │   │   │   return fn(*args, **kwargs)                                                                                                                                                                                                                                 │
│                                                                                                                                                                                                                                                                              │
│ /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/WayveCode/wayve/ai/lib/deploy.py:372 in compile_model                                                                                           │
│                                                                                                                                                                                                                                                                              │
│ ❱ 372 │   │   model_jit = torch.jit.script(                                                                                                                                                                                                                                  │
│                                                                                                                                                                                                                                                                              │
│ /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/pip-core_torch/site-packages/torch/jit/_script.py:1443 in script                                                                                │
│                                                                                                                                                                                                                                                                              │
│ ❱ 1443 │   │   ret = _script_impl(                                                                                                                                                                                                                                           │
│                                                                                                                                                                                                                                                                              │
│ /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/pip-core_torch/site-packages/torch/jit/_script.py:1152 in _script_impl                                                                          │
│                                                                                                                                                                                                                                                                              │
│ ❱ 1152 │   │   return torch.jit._recursive.create_script_module(                                                                                                                                                                                                             │
│                                                                                                                                                                                                                                                                              │
│ /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/pip-core_torch/site-packages/torch/jit/_recursive.py:556 in create_script_module                                                                │
│                                                                                                                                                                                                                                                                              │
│ ❱  556 │   return create_script_module_impl(nn_module, concrete_type, stubs_fn)                                                                                                                                                                                              │
│                                                                                                                                                                                                                                                                              │
│ /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/pip-core_torch/site-packages/torch/jit/_recursive.py:629 in create_script_module_impl                                                           │
│                                                                                                                                                                                                                                                                              │
│ ❱  629 │   │   create_methods_and_properties_from_stubs(                                                                                                                                                                                                                     │
│                                                                                                                                                                                                                                                                              │
│ /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/pip-core_torch/site-packages/torch/jit/_recursive.py:465 in create_methods_and_properties_from_stubs                                            │
│                                                                                                                                                                                                                                                                              │
│ ❱  465 │   concrete_type._create_methods_and_properties(                                                                                                                                                                                                                     │
│                                                                                                                                                                                                                                                                              │
│ /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/pip-core_torch/site-packages/torch/jit/_recursive.py:1026 in compile_unbound_method                                                             │
│                                                                                                                                                                                                                                                                              │
│ ❱ 1026 │   │   create_methods_and_properties_from_stubs(concrete_type, (stub,), ())                                                                                                                                                                                          │
│                                                                                                                                                                                                                                                                              │
│ /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/pip-core_torch/site-packages/torch/jit/_recursive.py:465 in create_methods_and_properties_from_stubs                                            │
│                                                                                                                                                                                                                                                                              │
│ ❱  465 │   concrete_type._create_methods_and_properties(                                                                                                                                                                                                                     │
│                                                                                                                                                                                                                                                                              │
│ /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/pip-core_torch/site-packages/torch/jit/_recursive.py:1026 in compile_unbound_method                                                             │
│                                                                                                                                                                                                                                                                              │
│ ❱ 1026 │   │   create_methods_and_properties_from_stubs(concrete_type, (stub,), ())                                                                                                                                                                                          │
│                                                                                                                                                                                                                                                                              │
│ /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/pip-core_torch/site-packages/torch/jit/_recursive.py:465 in create_methods_and_properties_from_stubs                                            │
│                                                                                                                                                                                                                                                                              │
│ ❱  465 │   concrete_type._create_methods_and_properties(                                                                                                                                                                                                                     │
│                                                                                                                                                                                                                                                                              │
│ /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/pip-core_torch/site-packages/torch/jit/_recursive.py:993 in try_compile_fn                                                                      │
│                                                                                                                                                                                                                                                                              │
│ ❱  993 │   return torch.jit.script(fn, _rcb=rcb)                                                                                                                                                                                                                             │
│                                                                                                                                                                                                                                                                              │
│ /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/pip-core_torch/site-packages/torch/jit/_script.py:1443 in script                                                                                │
│                                                                                                                                                                                                                                                                              │
│ ❱ 1443 │   │   ret = _script_impl(                                                                                                                                                                                                                                           │
│                                                                                                                                                                                                                                                                              │
│ /workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/pip-core_torch/site-packages/torch/jit/_script.py:1214 in _script_impl                                                                          │
│                                                                                                                                                                                                                                                                              │
│ ❱ 1214 │   │   fn = torch._C._jit_script_compile(                                                                                                                                                                                                                            │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
RuntimeError: 
attribute lookup is not defined on python value of type 'EnumTypeWrapper':
  File "/workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/WayveCode/wayve/ai/zoo/deployment/deployment_wrapper.py", line 1732
        # Require valid DrivePositionV2 values
        valid_positions = (
            DrivePositionV2.DRIVE_POSITION_V2_UNKNOWN,
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ <--- HERE
            DrivePositionV2.DRIVE_POSITION_V2_PARK,
            DrivePositionV2.DRIVE_POSITION_V2_NEUTRAL,
'_convert_gear_position_to_direction' is being compiled since it was called from 'ParkingDeploymentWrapper._add_vehicle_gear_direction_input'
  File "/workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/WayveCode/wayve/ai/zoo/deployment/deployment_wrapper.py", line 1794
    def _add_vehicle_gear_direction_input(self, dict_inputs: SiInputs, vehicle_gear_position: Tensor) -> SiInputs:
        """Add vehicle gear direction input derived from DrivePositionV2 gear position."""
        gear_direction = self._convert_gear_position_to_direction(vehicle_gear_position)
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ <--- HERE
        dict_inputs[DataKeys.VEHICLE_GEAR_DIRECTION] = gear_direction
        return dict_inputs
'ParkingDeploymentWrapper._add_vehicle_gear_direction_input' is being compiled since it was called from 'ParkingDeploymentWrapper._forward_with_additional_inputs'
  File "/workspace/.cache/bazel/63bf4bd60d62407ea3cc09dd362c8974/execroot/WayveCode/bazel-out/k8-opt/bin/wayve/ai/si/deploy.runfiles/WayveCode/wayve/ai/zoo/deployment/deployment_wrapper.py", line 1923
        )
    
        dict_inputs = self._add_vehicle_gear_direction_input(dict_inputs, vehicle_gear_position)
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ <--- HERE
        dict_inputs = self._add_driving_controls_inputs(dict_inputs, driving_controls)
    
'ParkingDeploymentWrapper._forward_with_additional_inputs' is being compiled since it was called from 'ParkingDeploymentWrapper.forward'
  File "/tmp/tmp1zak53xo/generated_wrapper.py", line 9
    def forward(self, camera_timestamp: Tensor, camera_images: Tensor, camera_intrinsics: Tensor, camera_extrinsics: Tensor, camera_distortion: Tensor, vehicle_timestamp: Tensor, vehicle_speed: Tensor, vehicle_curvature: Tensor, vehicle_pose: Tensor, map_speed_limit: 
Tensor, map_route: Tensor, vehicle_indicator_state: Tensor, gps_latitude_deg: Tensor, gps_longitude_deg: Tensor, vehicle_model: Tensor, vehicle_gear_position: Tensor, driving_controls: Tensor) -> OnBoardDrivingOutput:
        """Run on the vehicle without radar inputs."""
        return self._forward_with_additional_inputs(
               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            camera_timestamp=camera_timestamp,
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            camera_images=camera_images,
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            camera_intrinsics=camera_intrinsics,
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            camera_extrinsics=camera_extrinsics,
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            camera_distortion=camera_distortion,
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            vehicle_timestamp=vehicle_timestamp,
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            vehicle_speed=vehicle_speed,
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            vehicle_curvature=vehicle_curvature,
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            vehicle_pose=vehicle_pose,
            ~~~~~~~~~~~~~~~~~~~~~~~~~~
            map_speed_limit=map_speed_limit,
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            map_route=map_route,
            ~~~~~~~~~~~~~~~~~~~~
            vehicle_indicator_state=vehicle_indicator_state,
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            gps_latitude_deg=gps_latitude_deg,
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            gps_longitude_deg=gps_longitude_deg,
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            vehicle_model=vehicle_model,
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            vehicle_gear_position=vehicle_gear_position,
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            driving_controls=driving_controls,
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            radar_data=None,
            ~~~~~~~~~~~~~~~~
            radar_timestamp=None,
            ~~~~~~~~~~~~~~~~~~~~~
            radar_extrinsics=None,
            ~~~~~~~~~~~~~~~~~~~~~ <--- HERE
        )
```
