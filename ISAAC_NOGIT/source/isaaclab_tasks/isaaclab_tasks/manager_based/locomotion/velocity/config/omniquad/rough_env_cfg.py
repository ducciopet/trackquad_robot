from isaaclab.utils import configclass
import isaaclab_tasks.manager_based.locomotion.velocity.mdp as mdp
from isaaclab_tasks.manager_based.locomotion.velocity.velocity_env_omni_cfg import LocomotionVelocityRoughEnvCfg

##
# Pre-defined configs
##
from isaaclab_assets.robots.omniquad import OMNIQUAD_CFG  # isort: skip


@configclass
class OmniQuadRoughEnvCfg(LocomotionVelocityRoughEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()
        # switch robot to anymal-c
        self.scene.robot = OMNIQUAD_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")
