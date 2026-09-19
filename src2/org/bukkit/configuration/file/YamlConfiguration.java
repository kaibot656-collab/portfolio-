package org.bukkit.configuration.file;
import java.io.*;
public class YamlConfiguration extends FileConfiguration {
    public static YamlConfiguration loadConfiguration(java.io.File f) { return new YamlConfiguration(); }
    public void save(java.io.File f) throws IOException {}
    public void load(java.io.File f) throws Exception {}
}