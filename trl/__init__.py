# flake8: noqa

__version__ = "0.11.0.dev0"

from typing import TYPE_CHECKING
from .import_utils import _LazyModule, is_diffusers_available, OptionalDependencyNotAvailable

_import_structure = {
    "core": [
        "set_seed",
    ],
    "environment": [
        "TextEnvironment",
        "TextHistory",
    ],
    "extras": [
        "BestOfNSampler",
    ],
    "import_utils": [
        "is_bitsandbytes_available",
        "is_diffusers_available",
        "is_npu_available",
        "is_peft_available",
        "is_pil_available",
        "is_wandb_available",
        "is_xpu_available",
        "is_llmblender_available",
        "is_openai_available",
        "is_liger_available",
    ],
    "models": [
        "AutoModelForCausalLMWithValueHead",
        "AutoModelForSeq2SeqLMWithValueHead",
        "PreTrainedModelWrapper",
        "create_reference_model",
        "setup_chat_format",
        "SUPPORTED_ARCHITECTURES",
    ],
    "trainer": [
        "DataCollatorForCompletionOnlyLM",
        "DPOConfig",
        "DPOTrainer",
        "CPOConfig",
        "CPOTrainer",
        "AlignPropConfig",
        "AlignPropTrainer",
        "IterativeSFTTrainer",
        "KTOConfig",
        "KTOTrainer",
        "BCOConfig",
        "BCOTrainer",
        "ModelConfig",
        "OnlineDPOConfig",
        "OnlineDPOTrainer",
        "XPOConfig",
        "XPOTrainer",
        "ORPOConfig",
        "ORPOTrainer",
        "PPOConfig",
        "PPOTrainer",
        "PPOv2Config",
        "PPOv2Trainer",
        "RewardConfig",
        "RewardTrainer",
        "SFTConfig",
        "SFTTrainer",
        "FDivergenceConstants",
        "FDivergenceType",
        "WinRateCallback",
        "BaseJudge",
        "BaseRankJudge",
        "BasePairwiseJudge",
        "RandomRankJudge",
        "RandomPairwiseJudge",
        "PairRMJudge",
        "HfPairwiseJudge",
        "OpenAIPairwiseJudge",
    ],
    "commands": [],
    "commands.cli_utils": ["init_zero_verbose", "SFTScriptArguments", "DPOScriptArguments", "TrlParser"],
    "trainer.callbacks": ["RichProgressCallback", "SyncRefModelCallback"],
    "trainer.utils": ["get_kbit_device_map", "get_peft_config", "get_quantization_config"],
    "multitask_prompt_tuning": [
        "MultitaskPromptEmbedding",
        "MultitaskPromptTuningConfig",
        "MultitaskPromptTuningInit",
    ],
    "data_utils": ["maybe_reformat_dpo_to_kto"],
}

try:
    if not is_diffusers_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["models"].extend(
        [
            "DDPOPipelineOutput",
            "DDPOSchedulerOutput",
            "DDPOStableDiffusionPipeline",
            "DefaultDDPOStableDiffusionPipeline",
        ]
    )
    _import_structure["trainer"].extend(["DDPOConfig", "DDPOTrainer"])

if TYPE_CHECKING:
    from .core import set_seed
    from .environment import TextEnvironment, TextHistory
    from .extras import BestOfNSampler
    from .import_utils import (
        is_bitsandbytes_available,
        is_diffusers_available,
        is_npu_available,
        is_peft_available,
        is_pil_available,
        is_wandb_available,
        is_xpu_available,
        is_llmblender_available,
        is_openai_available,
        is_liger_available,
    )
    from .models import (
        AutoModelForCausalLMWithValueHead,
        AutoModelForSeq2SeqLMWithValueHead,
        PreTrainedModelWrapper,
        create_reference_model,
        setup_chat_format,
        SUPPORTED_ARCHITECTURES,
    )
    from .trainer import (
        DataCollatorForCompletionOnlyLM,
        DPOConfig,
        DPOTrainer,
        CPOConfig,
        CPOTrainer,
        AlignPropConfig,
        AlignPropTrainer,
        IterativeSFTTrainer,
        KTOConfig,
        KTOTrainer,
        BCOConfig,
        BCOTrainer,
        ModelConfig,
        OnlineDPOConfig,
        OnlineDPOTrainer,
        XPOConfig,
        XPOTrainer,
        ORPOConfig,
        ORPOTrainer,
        PPOConfig,
        PPOTrainer,
        PPOv2Config,
        PPOv2Trainer,
        RewardConfig,
        RewardTrainer,
        SFTConfig,
        SFTTrainer,
        FDivergenceConstants,
        FDivergenceType,
        WinRateCallback,
        BaseJudge,
        BaseRankJudge,
        BasePairwiseJudge,
        RandomRankJudge,
        RandomPairwiseJudge,
        PairRMJudge,
        HfPairwiseJudge,
        OpenAIPairwiseJudge,
    )
    from .trainer.callbacks import RichProgressCallback, SyncRefModelCallback
    from .trainer.utils import get_kbit_device_map, get_peft_config, get_quantization_config
    from .commands.cli_utils import init_zero_verbose, SFTScriptArguments, DPOScriptArguments, TrlParser
    from .data_utils import maybe_reformat_dpo_to_kto

    try:
        if not is_diffusers_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .models import (
            DDPOPipelineOutput,
            DDPOSchedulerOutput,
            DDPOStableDiffusionPipeline,
            DefaultDDPOStableDiffusionPipeline,
        )
        from .trainer import DDPOConfig, DDPOTrainer

else:
    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
        extra_objects={"__version__": __version__},
    )
