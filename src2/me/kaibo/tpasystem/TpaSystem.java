package me.kaibo.tpasystem;
import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.PluginCommand;
import org.bukkit.entity.Player;
import org.bukkit.entity.UUID;
import org.bukkit.event.Listener;
import org.bukkit.Bukkit;
import java.util.Map;
import java.util.HashMap;

public class TpaSystem extends JavaPlugin implements Listener {
    private Map<java.util.UUID, java.util.UUID> tpaRequests;

    public TpaSystem() {
        tpaRequests = new HashMap<>();
    }

    @Override
    public void onEnable() {
        Bukkit.getPluginManager().registerEvents(this, this);
        saveDefaultConfig();
        reloadConfig();
        PluginCommand tpa = new PluginCommand("tpa");
        tpa.setExecutor(new TpaCommand(this));
        registerCommand("tpa", tpa);
        PluginCommand tpaccept = new PluginCommand("tpaccept");
        tpaccept.setExecutor(new TpacceptCommand(this));
        registerCommand("tpaccept", tpaccept);
        PluginCommand tpdeny = new PluginCommand("tpdeny");
        tpdeny.setExecutor(new TpdenyCommand(this));
        registerCommand("tpdeny", tpdeny);
        PluginCommand tpcancel = new PluginCommand("tpcancel");
        tpcancel.setExecutor(new TpcancelCommand(this));
        registerCommand("tpcancel", tpcancel);
        PluginCommand tpahere = new PluginCommand("tpahere");
        tpahere.setExecutor(new TpahereCommand(this));
        registerCommand("tpahere", tpahere);
        getLogger().info("TpaSystem v1.0.0 by Sharky!");
    }

    @Override
    public void onDisable() {
        tpaRequests.clear();
    }

    public boolean onTpa(CommandSender s, Player target) {
        if (target == null) { s.sendMessage("Player not found."); return true; }
        if (target.getName().equals(s.getName())) { s.sendMessage("Cant tpa yourself!"); return true; }
        if (tpaRequests.containsKey(target.getUniqueId())) { s.sendMessage("Already has request."); return true; }
        tpaRequests.put(target.getUniqueId(), s.getUniqueId());
        s.sendMessage("Request sent to " + target.getName() + "!");
        target.sendMessage(s.getName() + " wants tp! /tpaccept");
        return true;
    }

    public boolean onTpaccept(Player p) {
        java.util.UUID fromId = tpaRequests.remove(p.getUniqueId());
        if (fromId == null) { p.sendMessage("No pending request!"); return true; }
        Player from = Bukkit.getPlayer(fromId.toString());
        if (from == null || !from.isOnline()) { p.sendMessage("Offline."); return true; }
        p.teleport(from.getLocation());
        from.sendMessage(p.getName() + " accepted!");
        p.sendMessage("Teleported!");
        return true;
    }

    public boolean onTpdeny(Player p) {
        java.util.UUID fromId = tpaRequests.remove(p.getUniqueId());
        if (fromId == null) { p.sendMessage("No pending request!"); return true; }
        Player from = Bukkit.getPlayer(fromId.toString());
        if (from != null && from.isOnline()) from.sendMessage(p.getName() + " denied.");
        p.sendMessage("Denied.");
        return true;
    }

    public boolean onTpcancel(Player p) {
        boolean found = false;
        for (java.util.UUID key : tpaRequests.keySet()) {
            if (tpaRequests.get(key).equals(p.getUniqueId())) { tpaRequests.remove(key); p.sendMessage("Cancelled."); found = true; break; }
        }
        if (!found) p.sendMessage("No pending request.");
        return true;
    }

    public boolean onTpahere(CommandSender s, Player target) {
        if (target == null) { s.sendMessage("Player not found."); return true; }
        tpaRequests.put(target.getUniqueId(), s.getUniqueId());
        s.sendMessage("Request sent to " + target.getName() + "!");
        target.sendMessage(s.getName() + " wants you here! /tpaccept");
        return true;
    }
}

class TpaCommand implements CommandExecutor {
    private TpaSystem plugin;
    TpaCommand(TpaSystem p) { this.plugin = p; }
    public boolean onCommand(CommandSender s, Command c, String l, String[] a) {
        if (!(s instanceof Player)) { s.sendMessage("Only players."); return true; }
        Player pl = (Player) s;
        if (a.length < 1) { pl.sendMessage("/tpa <player>"); return true; }
        return plugin.onTpa(pl, Bukkit.getPlayer(a[0]));
    }
}
class TpacceptCommand implements CommandExecutor {
    private TpaSystem plugin;
    TpacceptCommand(TpaSystem p) { this.plugin = p; }
    public boolean onCommand(CommandSender s, Command c, String l, String[] a) {
        if (!(s instanceof Player)) return true;
        return plugin.onTpaccept((Player) s);
    }
}
class TpdenyCommand implements CommandExecutor {
    private TpaSystem plugin;
    TpdenyCommand(TpaSystem p) { this.plugin = p; }
    public boolean onCommand(CommandSender s, Command c, String l, String[] a) {
        if (!(s instanceof Player)) return true;
        return plugin.onTpdeny((Player) s);
    }
}
class TpcancelCommand implements CommandExecutor {
    private TpaSystem plugin;
    TpcancelCommand(TpaSystem p) { this.plugin = p; }
    public boolean onCommand(CommandSender s, Command c, String l, String[] a) {
        if (!(s instanceof Player)) return true;
        return plugin.onTpcancel((Player) s);
    }
}
class TpahereCommand implements CommandExecutor {
    private TpaSystem plugin;
    TpahereCommand(TpaSystem p) { this.plugin = p; }
    public boolean onCommand(CommandSender s, Command c, String l, String[] a) {
        if (!(s instanceof Player)) return true;
        Player pl = (Player) s;
        if (a.length < 1) { pl.sendMessage("/tpahere <player>"); return true; }
        return plugin.onTpahere(pl, Bukkit.getPlayer(a[0]));
    }
}
