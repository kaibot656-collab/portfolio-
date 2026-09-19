package org.bukkit.plugin.java;
import org.bukkit.plugin.PluginDescriptionFile;
import org.bukkit.configuration.file.FileConfiguration;
import org.bukkit.command.PluginCommand;
import org.bukkit.command.CommandExecutor;
import org.bukkit.event.Listener;
import org.bukkit.plugin.Plugin;
import java.util.Map;
import java.util.HashMap;
public abstract class JavaPlugin implements org.bukkit.plugin.Plugin {
    private static JavaPlugin instance;
    private Map<String, PluginCommand> commands;
    public JavaPlugin() { commands = new HashMap<>(); }
    public void onEnable() {}
    public void onDisable() {}
    public static JavaPlugin getPlugin(Class<?> c) { return instance; }
    public java.util.logging.Logger getLogger() { return java.util.logging.Logger.getLogger(getClass().getName()); }
    public PluginCommand getCommand(String n) { return commands.get(n); }
    public void registerCommand(String name, PluginCommand cmd) { commands.put(name, cmd); }
    public void saveDefaultConfig() {}
    public FileConfiguration getConfig() { return null; }
    public void reloadConfig() {}
    public void saveConfig() {}
    public Object getPluginManager() { return null; }
    public void registerEvents(Listener l, Plugin p) {}
}