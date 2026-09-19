package org.bukkit.configuration.file;
import org.bukkit.configuration.Configuration;
public class FileConfiguration implements Configuration {
    public String getString(String p) { return null; }
    public String getString(String p, String d) { return d; }
    public int getInt(String p) { return 0; }
    public long getLong(String p, long d) { return d; }
    public void set(String p, Object v) {}
}