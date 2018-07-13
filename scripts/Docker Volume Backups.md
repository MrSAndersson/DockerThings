# Docker Volume Backups

## Backing up a volume
This backs up the volume "samplevolume" to /tmp/sample_archive.tar.bz2 on the host
```bash
docker run -it --rm -v samplevolume:/volume -v /tmp:/backup alpine \
    tar -cjf /backup/sample_archive.tar.bz2 -C /volume ./
```

## Restoring a volume

Replaces all content in "samplevolume" with the content in /tmp/sample_archive.tar.bz2 on the host

```bash
docker run -it --rm -v some_volume:/volume -v /tmp:/backup alpine \
    sh -c "rm -rf /volume/* /volume/..?* /volume/.[!.]* ; tar -C /volume/ -xjf /backup/some_archive.tar.bz2"
```