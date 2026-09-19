package org.bukkit.command;
public class PluginCommand {
    private String name;
    private CommandExecutor executor;
    public PluginCommand(String name) { this.name = name; }
    public void setExecutor(CommandExecutor executor) { this.executor = executor; }
    public String getName() { return name; }
    public String toString() { return name; }
}