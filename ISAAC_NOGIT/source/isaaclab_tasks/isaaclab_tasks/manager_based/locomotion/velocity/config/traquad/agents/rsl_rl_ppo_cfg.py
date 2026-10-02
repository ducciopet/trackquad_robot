from isaaclab.utils import configclass

from isaaclab_rl.rsl_rl import RslRlOnPolicyRunnerCfg, RslRlPpoActorCriticCfg, RslRlPpoAlgorithmCfg, RslRlPpoActorCriticRecurrentCfg


@configclass
class TraQuadRoughPPORunnerCfg(RslRlOnPolicyRunnerCfg):
    num_steps_per_env = 24
    max_iterations = 15000
    save_interval = 50
    experiment_name = "traquad_rough"
    empirical_normalization = False
    """ policy = RslRlPpoActorCriticCfg(
        init_noise_std=1.0,
        actor_hidden_dims=[512, 256, 128],
        critic_hidden_dims=[512, 256, 128],
        activation="elu",
    ) """

    algorithm = RslRlPpoAlgorithmCfg(
        value_loss_coef=1.0,
        use_clipped_value_loss=True,
        clip_param=0.2,
        entropy_coef=0.005,
        num_learning_epochs=5,
        num_mini_batches=4,
        learning_rate=5.0e-4,
        schedule="adaptive",
        gamma=0.99,
        lam=0.95,
        desired_kl=0.01,
        max_grad_norm=1.0,
    )

    policy = RslRlPpoActorCriticRecurrentCfg(

        init_noise_std=1.0,  # 2.0,

        noise_std_type="log",

        actor_obs_normalization=False,

        critic_obs_normalization=False,

        actor_hidden_dims=[256, 128, 64],

        critic_hidden_dims=[256, 128, 64],

        activation="elu",

        rnn_type="lstm",  # "gru",

        rnn_hidden_dim=256,

        rnn_num_layers=1,

    )



@configclass
class TraQuadFlatPPORunnerCfg(TraQuadRoughPPORunnerCfg):
    def __post_init__(self):
        super().__post_init__()

        self.max_iterations = 5000
        self.experiment_name = "traquad_flat"
        self.policy.actor_hidden_dims = [128, 128, 128]
        self.policy.critic_hidden_dims = [128, 128, 128]
        self.policy = RslRlPpoActorCriticRecurrentCfg(

            init_noise_std=2.0,  # 2.0,

            noise_std_type="log",

            actor_obs_normalization=False,

            critic_obs_normalization=False,

            actor_hidden_dims=[256, 128, 64],

            critic_hidden_dims=[256, 128, 64],

            activation="elu",

            rnn_type="lstm",  # "gru",

            rnn_hidden_dim=256,

            rnn_num_layers=1,

        )
 