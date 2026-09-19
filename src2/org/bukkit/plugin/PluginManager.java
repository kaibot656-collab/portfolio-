package org.bukkit.plugin;
import org.bukkit.event.Listener;
import org.bukkit.plugin.Plugin;
public interface PluginManager {
    void registerEvents(Listener listener, Plugin plugin);
}