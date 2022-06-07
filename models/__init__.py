import os
import importlib

module_path = os.path.dirname(os.path.abspath(__file__))
models = [f for f in os.listdir(module_path) if f.endswith(".py") and f != "__init__.py"]
__all__ = models
for model in models:
    importlib.import_module(".{}".format(model[:-3]), __name__)

print(
    "Imported models: %s" % ", ".join(models)
    if models
    else "No models avaiable in the models directory."
)
