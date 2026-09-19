package org.bukkit;
import org.bukkit.entity.Player;
import org.bukkit.plugin.PluginManager;
import java.util.List;
public class Bukkit {
    public static Server getServer() { return null; }
    public static PluginManager getPluginManager() { return null; }
    public static void broadcastMessage(String msg) {}
    public static org.bukkit.command.PluginCommand getPluginCommand(String name) { return null; }
    public static org.bukkit.entity.Player getPlayer(String name) { return null; }
    public static org.bukkit.entity.Player[] getOnlinePlayers() { return new org.bukkit.entity.Player[0]; }
}