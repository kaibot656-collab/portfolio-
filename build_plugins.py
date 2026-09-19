import os, subprocess, shutil, zipfile

base = r"C:\Users\kaibo\Downloads\portfollio"
src = os.path.join(base, "src2")
build = os.path.join(base, "build")

if os.path.exists(src): shutil.rmtree(src)
if os.path.exists(build): shutil.rmtree(build)
os.makedirs(src)
os.makedirs(build)

pkg_dirs = ["org/bukkit/command", "org/bukkit/entity", "org/bukkit/event",
            "org/bukkit/event/player", "org/bukkit/inventory",
            "org/bukkit/configuration/file", "org/bukkit/scoreboard",
            "org/bukkit/plugin/java", "me/kaibo/tpasystem", "me/kaibo/chatmanager"]
for sub in pkg_dirs:
    os.makedirs(os.path.join(src, *sub.split("/")), exist_ok=True)

stubs = {
    "org/bukkit/Bukkit.java": 'package org.bukkit;\nimport org.bukkit.entity.Player;\nimport org.bukkit.plugin.PluginManager;\nimport java.util.List;\npublic class Bukkit {\n    public static Server getServer() { return null; }\n    public static PluginManager getPluginManager() { return null; }\n    public static void broadcastMessage(String msg) {}\n    public static org.bukkit.command.PluginCommand getPluginCommand(String name) { return null; }\n    public static org.bukkit.entity.Player getPlayer(String name) { return null; }\n    public static org.bukkit.entity.Player[] getOnlinePlayers() { return new org.bukkit.entity.Player[0]; }\n}',
    "org/bukkit/Server.java": 'package org.bukkit;\nimport org.bukkit.entity.Player;\nimport java.util.List;\npublic class Server {\n    public List<Player> getOnlinePlayers() { return null; }\n    public Player getPlayer(String name) { return null; }\n    public org.bukkit.plugin.PluginManager getPluginManager() { return null; }\n    public org.bukkit.command.PluginCommand getPluginCommand(String name) { return null; }\n    public void dispatchCommand(org.bukkit.command.CommandSender sender, String command) {}\n}',
    "org/bukkit/command/CommandSender.java": 'package org.bukkit.command;\npublic class CommandSender {\n    public boolean hasPermission(String perm) { return true; }\n    public void sendMessage(String msg) {}\n    public String getName() { return "Console"; }\n    public java.util.UUID getUniqueId() { return null; }\n}',
    "org/bukkit/command/Command.java": 'package org.bukkit.command;\npublic class Command {\n    private String name;\n    public Command(String name) { this.name = name; }\n    public String getName() { return name; }\n    public boolean execute(CommandSender sender, String label, String[] args) { return false; }\n}',
    "org/bukkit/command/CommandExecutor.java": 'package org.bukkit.command;\npublic interface CommandExecutor {\n    boolean onCommand(CommandSender sender, Command command, String label, String[] args);\n}',
    "org/bukkit/command/PluginCommand.java": 'package org.bukkit.command;\npublic class PluginCommand {\n    private String name;\n    private CommandExecutor executor;\n    public PluginCommand(String name) { this.name = name; }\n    public void setExecutor(CommandExecutor executor) { this.executor = executor; }\n    public String getName() { return name; }\n    public String toString() { return name; }\n}',
    "org/bukkit/entity/Player.java": 'package org.bukkit.entity;\nimport java.util.UUID;\nimport org.bukkit.command.CommandSender;\npublic class Player extends CommandSender {\n    public String getName() { return "Player"; }\n    public void sendMessage(String msg) {}\n    public void teleport(Location loc) {}\n    public Location getLocation() { return new Location(null, 0, 0, 0); }\n    public UUID getUniqueId() { return null; }\n    public boolean isOnline() { return true; }\n    public void setPlayerListName(String name) {}\n}',
    "org/bukkit/entity/Location.java": 'package org.bukkit.entity;\npublic class Location {\n    public Location(Object world, double x, double y, double z) {}\n    public double getX() { return 0; }\n    public double getY() { return 0; }\n    public double getZ() { return 0; }\n}',
    "org/bukkit/entity/UUID.java": 'package org.bukkit.entity;\npublic class UUID {\n    public String toString() { return "00000000-0000-0000-0000-000000000000"; }\n}',
    "org/bukkit/event/Event.java": 'package org.bukkit.event;\npublic class Event {}',
    "org/bukkit/event/Listener.java": 'package org.bukkit.event;\npublic interface Listener {}',
    "org/bukkit/event/EventHandler.java": 'package org.bukkit.event;\nimport java.lang.annotation.*;\n@Retention(RetentionPolicy.RUNTIME)\n@Target(ElementType.METHOD)\npublic @interface EventHandler {\n    int priority() default 0;\n    boolean ignoreCancelled() default false;\n}',
    "org/bukkit/event/EventPriority.java": 'package org.bukkit.event;\npublic class EventPriority {\n    public static final EventPriority LOWEST = new EventPriority();\n    public static final EventPriority LOW = new EventPriority();\n    public static final EventPriority NORMAL = new EventPriority();\n    public static final EventPriority HIGH = new EventPriority();\n    public static final EventPriority HIGHEST = new EventPriority();\n    public static final EventPriority MONITOR = new EventPriority();\n}',
    "org/bukkit/event/HandlerList.java": 'package org.bukkit.event;\npublic class HandlerList {\n    public static void registerEvents(Object listener, Object plugin) {}\n    public void register(Object listener) {}\n    public void unregisterAll() {}\n}',
    "org/bukkit/event/player/PlayerJoinEvent.java": 'package org.bukkit.event.player;\nimport org.bukkit.entity.Player;\nimport org.bukkit.event.Event;\npublic class PlayerJoinEvent extends Event {\n    private Player player;\n    public PlayerJoinEvent(Player player) { this.player = player; }\n    public Player getPlayer() { return player; }\n}',
    "org/bukkit/event/player/PlayerQuitEvent.java": 'package org.bukkit.event.player;\nimport org.bukkit.entity.Player;\nimport org.bukkit.event.Event;\npublic class PlayerQuitEvent extends Event {\n    private Player player;\n    public PlayerQuitEvent(Player player) { this.player = player; }\n    public Player getPlayer() { return player; }\n}',
    "org/bukkit/event/player/PlayerChatEvent.java": 'package org.bukkit.event.player;\nimport org.bukkit.entity.Player;\nimport org.bukkit.event.Event;\npublic class PlayerChatEvent extends Event {\n    private Player player;\n    private String message;\n    public PlayerChatEvent(Player player, String message) { this.player = player; this.message = message; }\n    public Player getPlayer() { return player; }\n    public String getMessage() { return message; }\n    public void setMessage(String msg) { this.message = msg; }\n    public void setCancelled(boolean c) {}\n    public boolean isCancelled() { return false; }\n    public void setFormat(String f) {}\n    public String getFormat() { return null; }\n}',
    "org/bukkit/event/player/PlayerCommandPreprocessEvent.java": 'package org.bukkit.event.player;\nimport org.bukkit.entity.Player;\nimport org.bukkit.event.Event;\npublic class PlayerCommandPreprocessEvent extends Event {\n    private Player player;\n    private String message;\n    public PlayerCommandPreprocessEvent(Player p, String m) { this.player = p; this.message = m; }\n    public Player getPlayer() { return player; }\n    public String getMessage() { return message; }\n    public void setCancelled(boolean c) {}\n    public boolean isCancelled() { return false; }\n}',
    "org/bukkit/event/player/PlayerTeleportEvent.java": 'package org.bukkit.event.player;\nimport org.bukkit.entity.Player;\nimport org.bukkit.entity.Location;\nimport org.bukkit.event.Event;\npublic class PlayerTeleportEvent extends Event {\n    private Player player;\n    private Location from, to;\n    public PlayerTeleportEvent(Player p, Location f, Location t) { this.player = p; this.from = f; this.to = t; }\n    public Player getPlayer() { return player; }\n    public Location getFrom() { return from; }\n    public Location getTo() { return to; }\n}',
    "org/bukkit/inventory/Inventory.java": 'package org.bukkit.inventory;\npublic class Inventory {\n    public int getSize() { return 0; }\n    public String getTitle() { return null; }\n    public ItemStack getItem(int slot) { return null; }\n    public void setItem(int slot, ItemStack item) {}\n}',
    "org/bukkit/inventory/ItemStack.java": 'package org.bukkit.inventory;\npublic class ItemStack {}',
    "org/bukkit/inventory/ItemMeta.java": 'package org.bukkit.inventory;\npublic class ItemMeta {}',
    "org/bukkit/configuration/Configuration.java": 'package org.bukkit.configuration;\npublic interface Configuration {}',
    "org/bukkit/configuration/file/FileConfiguration.java": 'package org.bukkit.configuration.file;\nimport org.bukkit.configuration.Configuration;\npublic class FileConfiguration implements Configuration {\n    public String getString(String p) { return null; }\n    public String getString(String p, String d) { return d; }\n    public int getInt(String p) { return 0; }\n    public long getLong(String p, long d) { return d; }\n    public void set(String p, Object v) {}\n}',
    "org/bukkit/configuration/file/YamlConfiguration.java": 'package org.bukkit.configuration.file;\nimport java.io.*;\npublic class YamlConfiguration extends FileConfiguration {\n    public static YamlConfiguration loadConfiguration(java.io.File f) { return new YamlConfiguration(); }\n    public void save(java.io.File f) throws IOException {}\n    public void load(java.io.File f) throws Exception {}\n}',
    "org/bukkit/scoreboard/ScoreboardManager.java": 'package org.bukkit.scoreboard;\npublic class ScoreboardManager {}',
    "org/bukkit/scoreboard/Scoreboard.java": 'package org.bukkit.scoreboard;\npublic class Scoreboard {}',
    "org/bukkit/scoreboard/Objective.java": 'package org.bukkit.scoreboard;\npublic class Objective {\n    public void setDisplayName(String n) {}\n    public String getDisplayName() { return null; }\n}',
    "org/bukkit/plugin/Plugin.java": 'package org.bukkit.plugin;\npublic interface Plugin {}',
    "org/bukkit/plugin/PluginManager.java": 'package org.bukkit.plugin;\nimport org.bukkit.event.Listener;\nimport org.bukkit.plugin.Plugin;\npublic interface PluginManager {\n    void registerEvents(Listener listener, Plugin plugin);\n}',
    "org/bukkit/plugin/PluginDescriptionFile.java": 'package org.bukkit.plugin;\npublic class PluginDescriptionFile {\n    public PluginDescriptionFile(String n, String v) {}\n    public String getName() { return "Plugin"; }\n    public String getVersion() { return "1.0"; }\n}',
    "org/bukkit/plugin/java/JavaPlugin.java": 'package org.bukkit.plugin.java;\nimport org.bukkit.plugin.PluginDescriptionFile;\nimport org.bukkit.configuration.file.FileConfiguration;\nimport org.bukkit.command.PluginCommand;\nimport org.bukkit.command.CommandExecutor;\nimport org.bukkit.event.Listener;\nimport org.bukkit.plugin.Plugin;\nimport java.util.Map;\nimport java.util.HashMap;\npublic abstract class JavaPlugin implements org.bukkit.plugin.Plugin {\n    private static JavaPlugin instance;\n    private Map<String, PluginCommand> commands;\n    public JavaPlugin() { commands = new HashMap<>(); }\n    public void onEnable() {}\n    public void onDisable() {}\n    public static JavaPlugin getPlugin(Class<?> c) { return instance; }\n    public java.util.logging.Logger getLogger() { return java.util.logging.Logger.getLogger(getClass().getName()); }\n    public PluginCommand getCommand(String n) { return commands.get(n); }\n    public void registerCommand(String name, PluginCommand cmd) { commands.put(name, cmd); }\n    public void saveDefaultConfig() {}\n    public FileConfiguration getConfig() { return null; }\n    public void reloadConfig() {}\n    public void saveConfig() {}\n    public Object getPluginManager() { return null; }\n    public void registerEvents(Listener l, Plugin p) {}\n}',
}

for path, content in stubs.items():
    full_path = os.path.join(src, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)

tpasystem_src = '''package me.kaibo.tpasystem;
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
'''

chatmanager_src = '''package me.kaibo.chatmanager;
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
'''

with open(os.path.join(src, "me/kaibo/tpasystem", "TpaSystem.java"), 'w') as f:
    f.write(tpasystem_src)

with open(os.path.join(src, "me/kaibo/chatmanager", "ChatManager.java"), 'w') as f:
    f.write(chatmanager_src)

# Compile
java_files = []
for root, dirs, files in os.walk(src):
    for f in files:
        if f.endswith('.java'):
            java_files.append(os.path.join(root, f))

errors = 0
for f in java_files:
    result = subprocess.run(['javac', '-cp', src, '-d', build, f], capture_output=True, text=True, cwd=src)
    if result.returncode != 0:
        errors += 1
        print(f"ERROR: {os.path.basename(f)}")
        print(result.stderr[:500])
    else:
        print(f"OK: {os.path.basename(f)}")

print(f"{errors} compile errors.")

# Build JARs
plugins = [("TpaSystem", "me.kaibo.tpasystem.TpaSystem"), ("ChatManager", "me.kaibo.chatmanager.ChatManager")]

plugin_yml_data = {
    "TpaSystem": "name: TpaSystem\nversion: 1.0.0\nmain: me.kaibo.tpasystem.TpaSystem\napi-version: 1.20\nauthor: Sharky\n",
    "ChatManager": "name: ChatManager\nversion: 1.0.0\nmain: me.kaibo.chatmanager.ChatManager\napi-version: 1.20\nauthor: Sharky\n",
}

config_yml_data = {
    "TpaSystem": "# TpaSystem Configuration\ncooldown-seconds: 60\n",
    "ChatManager": "# ChatManager Configuration\ndefault-channel: global\n",
}

for plugin_name, main_class in plugins:
    jar_path = os.path.join(base, f"{plugin_name}.jar")
    pkg_dir = os.path.join(build, *main_class.replace(".", os.sep).split(os.sep)[:-1])
    os.makedirs(pkg_dir, exist_ok=True)

    with open(os.path.join(build, "plugin.yml"), 'w') as f:
        f.write(plugin_yml_data[plugin_name])

    with open(os.path.join(build, "paper-plugin.yml"), 'w') as f:
        f.write(f"name: {plugin_name}\nversion: 1.0.0\nmain: {main_class}\napi-version: 1.21\nauthor: Sharky\ndescription: Plugin by Sharky\n")

    with open(os.path.join(build, "config.yml"), 'w') as f:
        f.write(config_yml_data[plugin_name])

    messages_dir = os.path.join(pkg_dir, "messages")
    os.makedirs(messages_dir, exist_ok=True)
    with open(os.path.join(messages_dir, "messages.yml"), 'w') as f:
        f.write(f"messages:\n  loaded: '&a{plugin_name} v1.0.0 loaded!'\n")

    manifest_content = f"Manifest-Version: 1.0\nMain-Class: {main_class}\n\n"

    with zipfile.ZipFile(jar_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("paper-plugin.yml", f"name: {plugin_name}\nversion: 1.0.0\nmain: {main_class}\napi-version: 1.21\nauthor: Sharky\ndescription: Plugin by Sharky\n")
        zf.writestr("plugin.yml", plugin_yml_data[plugin_name])
        zf.writestr("config.yml", config_yml_data[plugin_name])
        zf.writestr("META-INF/MANIFEST.MF", manifest_content)
        for root, dirs, files in os.walk(build):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, build)
                if arcname not in ["paper-plugin.yml", "plugin.yml", "config.yml", "META-INF/MANIFEST.MF"]:
                    zf.write(filepath, arcname)

    print(f"Created: {plugin_name}.jar ({os.path.getsize(jar_path)} bytes)")

# Verify
print("\nVerification:")
for plugin_name, main_class in plugins:
    jar_path = os.path.join(base, f"{plugin_name}.jar")
    with zipfile.ZipFile(jar_path) as zf:
        names = zf.namelist()
        root = [n for n in names if '/' not in n]
        print(f"{plugin_name}: root={root}")
        print(f"  commands in plugin.yml: {'commands:' in plugin_yml_data[plugin_name]}")

print("\nDone!")
