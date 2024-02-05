"""
Entry point for the FRESCO plugin
"""

from HorusAPI import Plugin


def createPlugin():
    """
    Generates the FRESCO plugin and returns the instance
    """
    # ========== Plugin Definition ========== #

    frescoPlugin = Plugin(id="FRESCO")

    # ========== Blocks ========== #
    from Blocks.AlphaFoldEAPM import alphafoldBlock  # type: ignore

    # Add the block to the plugin
    frescoPlugin.addBlock(alphafoldBlock)



    # Return the plugin
    return frescoPlugin


plugin = createPlugin()
