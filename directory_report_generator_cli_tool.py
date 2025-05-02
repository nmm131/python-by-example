from pathlib import Path
import argparse
import hashlib
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

# Setup logging at the top of your file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

def format_size(bytes_size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024

def compute_hash(file_path):
    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {e}")
        return None

def process_files(path):
    num_files = 0
    num_dirs = 0
    list_of_files = []
    list_of_empty_files = []
    extension_counts = {}
    file_hashes = {}

    # Iterate over all files in the directory
    for file in Path(path).rglob("*"):
        if file.is_file():
            num_files += 1
            file_size = file.stat().st_size
            list_of_files.append((str(file), file_size))
            
            # Track empty files
            if file.stat().st_size == 0:
                list_of_empty_files.append(file)
            
            # Track file extension
            ext = file.suffix.lower() or "[no extension]"
            extension_counts[ext] = extension_counts.get(ext, 0) + 1
        else:
            num_dirs += 1
        
    return num_files, num_dirs, list_of_files, list_of_empty_files, extension_counts

def compute_hashes_parallel(files):
    file_hashes = {}
    
    # Prepare to compute hashes in parallel
    with ThreadPoolExecutor() as executor:
        future_to_file = {executor.submit(compute_hash, file): file for file in files}
        for future in as_completed(future_to_file):
            file = future_to_file[future]
            try:
                file_hash = future.result()
                if file_hash:
                    file_str = str(file)
                    if file_hash in file_hashes:
                        file_hashes[file_hash].append(file_str)
                    else:
                        file_hashes[file_hash] = [file_str]
            except Exception as e:
                logger.error(f"Error computing hash for {file}: {e}")
    return file_hashes

def print_results(path, num_files, num_dirs, list_of_files, list_of_empty_files, extension_counts, file_hashes):
    # Arguments
    logger.info(f"Args: {path}")

    # Total size of all files
    total_size = sum(size for _, size in list_of_files)
    logger.info(f"Total size of all files: {format_size(total_size)}")
    logger.info(f"Number of files: {num_files}")
    logger.info(f"Number of directories: {num_dirs}")

    # Top 5 largest files
    largest_files = sorted(list_of_files, key=lambda x: x[1], reverse=True)[:5]
    logger.info(f"\nTop 5 largest files:")
    for filepath, size in largest_files:
        logger.info(f"{filepath}: {format_size(size)}")

    # List of empty files
    logger.info("Empty files:")
    for f in list_of_empty_files:
        logger.info(f"  {f}")

    # File extension counts
    logger.info("\nFile extension counts:")
    for ext, count in extension_counts.items():
        logger.info(f"{ext}: {count}")
    
    # Duplicate files based on hash
    logger.info("\nDuplicate files:")
    for file_hash, files in file_hashes.items():
        if len(files) > 1:
            logger.info(f"Hash: {file_hash}")
            for f in files:
                logger.info(f"    {f}")

def main():
    # Setup command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", default=Path.cwd(), help="Path")
    args = parser.parse_args()
    path = args.path

    # Check if path exists and is a directory
    if Path(path).exists() and Path(path).is_dir():
        logger.info("Path exists and is a directory!")
        num_files, num_dirs, list_of_files, list_of_empty_files, extension_counts = process_files(path)
        file_paths = [f for f, _ in list_of_files]
        file_hashes = compute_hashes_parallel(file_paths)
        print_results(path, num_files, num_dirs, list_of_files, list_of_empty_files, extension_counts, file_hashes)
    else:
        logger.warning("Path doesn't exist or isn't a directory.")

if __name__ == "__main__":
    main()