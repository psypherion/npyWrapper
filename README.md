# npyWrapper
npyWrapper is a high-performance Rust-based wrapper for `.npy` files, designed to overcome limitations in scalability, concurrency, and querying, making `.npy` files a viable alternative to vector databases in production. This wrapper supports advanced features like efficient data partitioning, metadata indexing, cloud integration, and redundancy, providing a resilient, cloud-ready solution for storing and querying high-dimensional data.

___

## Features
1. **Enhanced Scalability**
Dynamic Data Partitioning: Allows `.npy` datasets to be partitioned for efficient handling of large-scale data, preventing the need to reload entire files with each update.
Optimized Storage Structure: Efficiently organizes data across multiple `.npy` files to handle large datasets with minimal latency.

3. **Concurrency and Multi-User Access**
Concurrency Support: Designed with Rust’s memory safety and concurrency capabilities, allowing multiple users to read or write without data corruption.
Access Control: Customizable access levels provide fine-grained control over read and write permissions for multi-user environments.

5. **Advanced Querying and Search**
Metadata Indexing: Attaches searchable metadata to `.npy` files, enabling users to filter data based on attributes without loading entire files.
Approximate Nearest Neighbors (ANN): Integrated ANN search algorithms allow for efficient similarity searches directly on .npy data.
Flexible Query API: User-friendly query API supporting chained queries and filtering.

7. **Cloud Integration and Backup**
Seamless Cloud Storage Support: Works with major cloud providers like AWS S3 and Google Cloud Storage, enabling scalable, distributed storage.
Automatic Backup and Replication: Built-in options for periodic backups and replication, ensuring data durability and easy restoration.

9. **Reliability and Fault Tolerance**
Redundant Storage Mechanisms: Ensures data remains accessible, even in case of partial failures, with redundancy options.
Automatic Recovery: Fault-tolerant protocols recover lost or corrupted data segments from backups.
