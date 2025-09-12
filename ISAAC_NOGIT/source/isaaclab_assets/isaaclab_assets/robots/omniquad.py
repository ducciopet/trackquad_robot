from isaaclab_assets.sensors.velodyne import VELODYNE_VLP_16_RAYCASTER_CFG

import isaaclab.sim as sim_utils
from isaaclab.actuators import ActuatorNetLSTMCfg, DCMotorCfg, ImplicitActuatorCfg, IdealPDActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
from isaaclab.sensors import RayCasterCfg
from isaaclab.utils.assets import ISAACLAB_NUCLEUS_DIR

##
# Configuration - Actuators.
##

OMNIQUAD_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path="/home/duccio/Desktop/trackquad_robot/ISAAC_NOGIT/isaac_model/omniquad/omniquad.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True, solver_position_iteration_count=4, solver_velocity_iteration_count=0
        ),
        # collision_props=sim_utils.CollisionPropertiesCfg(contact_offset=0.02, rest_offset=0.0),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.4),
        joint_pos={
            # Left legs
            "LF_HFE": 2.0,
            "LH_HFE": -2.0,
            "LF_KFE": -1.2,
            "LH_KFE": 1.2,
            # Right legs
            "RF_HFE": -2.0,
            "RH_HFE": 2.0,
            "RF_KFE": 1.2,
            "RH_KFE": -1.2,
            # Wheels
            "LF_ANKLE": 0.0,
            "LH_ANKLE": 0.0,
            "RF_ANKLE": 0.0,
            "RH_ANKLE": 0.0,
        },
        joint_vel={".*": 0.0},
    ),
    actuators={"legs": ImplicitActuatorCfg(
            joint_names_expr=[".*HFE", ".*KFE"],
            effort_limit_sim=5.0,
            velocity_limit_sim=10.0,
            stiffness={
                ".*HFE": 10.7,
                ".*KFE": 10.7,
            
            },
            damping={
                ".*HFE": 0.1,
                ".*KFE": 0.1,
                
            },
        ),
        "wheels": ImplicitActuatorCfg(
            joint_names_expr=[".*ANKLE"],
            effort_limit_sim=500.0,
            velocity_limit_sim=1000.0,
            stiffness={
                ".*ANKLE": 0.0},
            damping={
                ".*ANKLE": 1.0,},
        )},
    soft_joint_pos_limit_factor=0.95,
)
