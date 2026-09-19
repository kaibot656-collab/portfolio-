package me.kaibo.chatmanager;
import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.PluginCommand;
import org.bukkit.entity.Player;
import org.bukkit.event.Listener;
import org.bukkit.Bukkit;
import java.util.Map;
import java.util.HashMap;

public class ChatManager extends JavaPlugin implements Listener {
    private Map<java.util.UUID, String> channels;
    private Map<java.util.UUID, Boolean> spyMode;

    public ChatManager() {
        channels = new HashMap<>();
        spyMode = new HashMap<>();
    }

    @Override
    public void onEnable() {
        Bukkit.getPluginManager().registerEvents(this, this);
        saveDefaultConfig();
        PluginCommand chat = new PluginCommand("chat");
        chat.setExecutor(new ChatCommand(this));
        registerCommand("chat", chat);
        PluginCommand spy = new PluginCommand("spy");
        spy.setExecutor(new SpyCommand(this));
        registerCommand("spy", spy);
        PluginCommand nick = new PluginCommand("nick");
        nick.setExecutor(new NickCommand(this));
        registerCommand("nick", nick);
        getLogger().info("ChatManager v1.0.0 by Sharky!");
    }

    @Override
    public void onDisable() {
        channels.clear();
        spyMode.clear();
    }

    public boolean onChat(CommandSender s, String channel) {
        if (!(s instanceof Player)) return true;
        Player p = (Player) s;
        channels.put(p.getUniqueId(), channel);
        p.sendMessage("Chat: " + channel.toUpperCase());
        return true;
    }

    public boolean onSpy(Player p) {
        boolean isSpy = spyMode.getOrDefault(p.getUniqueId(), false);
        spyMode.put(p.getUniqueId(), !isSpy);
        p.sendMessage("Spy: " + (!isSpy ? "ON" : "OFF"));
        return true;
    }

    public boolean onNick(Player p, String name) {
        p.setPlayerListName(name);
        p.sendMessage("Nick: " + name);
        return true;
    }
}

class ChatCommand implements CommandExecutor {
    private ChatManager plugin;
    ChatCommand(ChatManager p) { this.plugin = p; }
    public boolean onCommand(CommandSender s, Command c, String l, String[] a) {
        if (a.length < 1) { s.sendMessage("/chat <global|local|admin>"); return true; }
        return plugin.onChat(s, a[0]);
    }
}
class SpyCommand implements CommandExecutor {
    private ChatManager plugin;
    SpyCommand(ChatManager p) { this.plugin = p; }
    public boolean onCommand(CommandSender s, Command c, String l, String[] a) {
        if (!(s instanceof Player)) return true;
        return plugin.onSpy((Player) s);
    }
}
class NickCommand implements CommandExecutor {
    private ChatManager plugin;
    NickCommand(ChatManager p) { this.plugin = p; }
    public boolean onCommand(CommandSender s, Command c, String l, String[] a) {
        if (a.length < 1) { s.sendMessage("/nick <name>"); return true; }
        if (!(s instanceof Player)) return true;
        return plugin.onNick((Player) s, a[0]);
    }
}
