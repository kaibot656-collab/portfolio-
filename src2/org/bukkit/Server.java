package org.bukkit;
import org.bukkit.entity.Player;
import java.util.List;
public class Server {
    public List<Player> getOnlinePlayers() { return null; }
    public Player getPlayer(String name) { return null; }
    public org.bukkit.plugin.PluginManager getPluginManager() { return null; }
    public org.bukkit.command.PluginCommand getPluginCommand(String name) { return null; }
    public void dispatchCommand(org.bukkit.command.CommandSender sender, String command) {}
}