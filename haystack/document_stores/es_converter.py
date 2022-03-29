from typing import Optional, List


def open_search_index_to_document_store(
    document_store: "BaseDocumentStore",
    original_index_name: str,
    original_content_field: str,
    original_name_field: Optional[str] = None,
    included_metadata_fields: Optional[List[str]] = None,
    excluded_metadata_fields: Optional[List[str]] = None,
    store_original_ids: bool = True,
    index: Optional[str] = None,
    preprocessor: Optional[PreProcessor] = None,
    batch_size: int = 10_000,
    host: Union[str, List[str]] = "localhost",
    port: Union[int, List[int]] = 9200,
    username: str = "admin",
    password: str = "admin",
    api_key_id: Optional[str] = None,
    api_key: Optional[str] = None,
    aws4auth=None,
    scheme: str = "https",
    ca_certs: Optional[str] = None,
    verify_certs: bool = False,
    timeout: int = 30,
    use_system_proxy: bool = False,
) -> "BaseDocumentStore":
    """
    This function provides brownfield support of existing OpenSearch indexes by converting each of the records in
    the provided index to haystack `Document` objects and writing them to the specified `DocumentStore`. It can be used
    on a regular basis in order to add new records of the OpenSearch index to the `DocumentStore`.

    :param document_store: The haystack `DocumentStore` to write the converted `Document` objects to.
    :param original_index_name: OpenSearch index containing the records to be converted.
    :param original_content_field: OpenSearch field containing the text to be put in the `content` field of the
        resulting haystack `Document` objects.
    :param original_name_field: Optional OpenSearch field containing the title of the Document.
    :param included_metadata_fields: List of OpenSearch fields that shall be stored in the `meta` field of the
        resulting haystack `Document` objects. If `included_metadata_fields` and `excluded_metadata_fields` are `None`,
        all the fields found in the OpenSearch records will be kept as metadata. You can specify only one of the
        `included_metadata_fields` and `excluded_metadata_fields` parameters.
    :param excluded_metadata_fields: List of OpenSearch fields that shall be excluded from the `meta` field of the
        resulting haystack `Document` objects. If `included_metadata_fields` and `excluded_metadata_fields` are `None`,
        all the fields found in the OpenSearch records will be kept as metadata. You can specify only one of the
        `included_metadata_fields` and `excluded_metadata_fields` parameters.
    :param store_original_ids: Whether to store the ID a record had in the original OpenSearch index at the
        `"_original_es_id"` metadata field of the resulting haystack `Document` objects. This should be set to `True`
        if you want to continuously update the `DocumentStore` with new records inside your OpenSearch index. If this
        parameter was set to `False` on the first call of `open_search_index_to_document_store`,
        all the indexed Documents in the `DocumentStore` will be overwritten in the second call.
    :param index: Name of index in `document_store` to use to store the resulting haystack `Document` objects.
    :param preprocessor: Optional PreProcessor that will be applied on the content field of the original OpenSearch
        record.
    :param batch_size: Number of records to process at once.
    :param host: URL(s) of OpenSearch nodes.
    :param port: Ports(s) of OpenSearch nodes.
    :param username: Username (standard authentication via http_auth).
    :param password: Password (standard authentication via http_auth).
    :param api_key_id: ID of the API key (altenative authentication mode to the above http_auth).
    :param api_key: Secret value of the API key (altenative authentication mode to the above http_auth).
    :param aws4auth: Authentication for usage with AWS OpenSearch
        (can be generated with the requests-aws4auth package).
    :param scheme: `"https"` or `"http"`, protocol used to connect to your OpenSearch instance.
    :param ca_certs: Root certificates for SSL: it is a path to certificate authority (CA) certs on disk.
        You can use certifi package with `certifi.where()` to find where the CA certs file is located in your machine.
    :param verify_certs: Whether to be strict about ca certificates.
    :param timeout: Number of seconds after which an OpenSearch request times out.
    :param use_system_proxy: Whether to use system proxy.
    """

    return elasticsearch_index_to_document_store(
        document_store=document_store,
        original_index_name=original_index_name,
        original_content_field=original_content_field,
        original_name_field=original_name_field,
        included_metadata_fields=included_metadata_fields,
        excluded_metadata_fields=excluded_metadata_fields,
        store_original_ids=store_original_ids,
        index=index,
        preprocessor=preprocessor,
        batch_size=batch_size,
        host=host,
        port=port,
        username=username,
        password=password,
        api_key_id=api_key_id,
        api_key=api_key,
        aws4auth=aws4auth,
        scheme=scheme,
        ca_certs=ca_certs,
        verify_certs=verify_certs,
        timeout=timeout,
        use_system_proxy=use_system_proxy,
    )


def elasticsearch_index_to_document_store(
    document_store: "BaseDocumentStore",
    original_index_name: str,
    original_content_field: str,
    original_name_field: Optional[str] = None,
    included_metadata_fields: Optional[List[str]] = None,
    excluded_metadata_fields: Optional[List[str]] = None,
    store_original_ids: bool = True,
    index: Optional[str] = None,
    preprocessor: Optional[PreProcessor] = None,
    batch_size: int = 10_000,
    host: Union[str, List[str]] = "localhost",
    port: Union[int, List[int]] = 9200,
    username: str = "",
    password: str = "",
    api_key_id: Optional[str] = None,
    api_key: Optional[str] = None,
    aws4auth=None,
    scheme: str = "http",
    ca_certs: Optional[str] = None,
    verify_certs: bool = True,
    timeout: int = 30,
    use_system_proxy: bool = False,
) -> "BaseDocumentStore":
    """
    This function provides brownfield support of existing Elasticsearch indexes by converting each of the records in
    the provided index to haystack `Document` objects and writing them to the specified `DocumentStore`. It can be used
    on a regular basis in order to add new records of the Elasticsearch index to the `DocumentStore`.

    :param document_store: The haystack `DocumentStore` to write the converted `Document` objects to.
    :param original_index_name: Elasticsearch index containing the records to be converted.
    :param original_content_field: Elasticsearch field containing the text to be put in the `content` field of the
        resulting haystack `Document` objects.
    :param original_name_field: Optional Elasticsearch field containing the title of the Document.
    :param included_metadata_fields: List of Elasticsearch fields that shall be stored in the `meta` field of the
        resulting haystack `Document` objects. If `included_metadata_fields` and `excluded_metadata_fields` are `None`,
        all the fields found in the Elasticsearch records will be kept as metadata. You can specify only one of the
        `included_metadata_fields` and `excluded_metadata_fields` parameters.
    :param excluded_metadata_fields: List of Elasticsearch fields that shall be excluded from the `meta` field of the
        resulting haystack `Document` objects. If `included_metadata_fields` and `excluded_metadata_fields` are `None`,
        all the fields found in the Elasticsearch records will be kept as metadata. You can specify only one of the
        `included_metadata_fields` and `excluded_metadata_fields` parameters.
    :param store_original_ids: Whether to store the ID a record had in the original Elasticsearch index at the
        `"_original_es_id"` metadata field of the resulting haystack `Document` objects. This should be set to `True`
        if you want to continuously update the `DocumentStore` with new records inside your Elasticsearch index. If this
        parameter was set to `False` on the first call of `elasticsearch_index_to_document_store`,
        all the indexed Documents in the `DocumentStore` will be overwritten in the second call.
    :param index: Name of index in `document_store` to use to store the resulting haystack `Document` objects.
    :param preprocessor: Optional PreProcessor that will be applied on the content field of the original Elasticsearch
        record.
    :param batch_size: Number of records to process at once.
    :param host: URL(s) of Elasticsearch nodes.
    :param port: Ports(s) of Elasticsearch nodes.
    :param username: Username (standard authentication via http_auth).
    :param password: Password (standard authentication via http_auth).
    :param api_key_id: ID of the API key (altenative authentication mode to the above http_auth).
    :param api_key: Secret value of the API key (altenative authentication mode to the above http_auth).
    :param aws4auth: Authentication for usage with AWS Elasticsearch
        (can be generated with the requests-aws4auth package).
    :param scheme: `"https"` or `"http"`, protocol used to connect to your Elasticsearch instance.
    :param ca_certs: Root certificates for SSL: it is a path to certificate authority (CA) certs on disk.
        You can use certifi package with `certifi.where()` to find where the CA certs file is located in your machine.
    :param verify_certs: Whether to be strict about ca certificates.
    :param timeout: Number of seconds after which an Elasticsearch request times out.
    :param use_system_proxy: Whether to use system proxy.
    """
    # This import cannot be at the beginning of the file, as this would result in a circular import
    from haystack.document_stores.elasticsearch import ElasticsearchDocumentStore

    # Initialize Elasticsearch client
    es_client = ElasticsearchDocumentStore._init_elastic_client(
        host=host,
        port=port,
        username=username,
        password=password,
        api_key=api_key,
        api_key_id=api_key_id,
        aws4auth=aws4auth,
        scheme=scheme,
        ca_certs=ca_certs,
        verify_certs=verify_certs,
        timeout=timeout,
        use_system_proxy=use_system_proxy,
    )

    # Get existing original ES IDs inside DocumentStore in order to not reindex the corresponding records
    existing_ids = [
        doc.meta["_original_es_id"]
        for doc in document_store.get_all_documents_generator(index=index)
        if "_original_es_id" in doc.meta
    ]

    # Iterate over each individual record
    query: Dict[str, Dict] = {"query": {"bool": {"must": [{"match_all": {}}]}}}
    if existing_ids:
        filters = LogicalFilterClause.parse({"_id": {"$nin": existing_ids}}).convert_to_elasticsearch()
        query["query"]["bool"]["filter"] = filters
    records = scan(client=es_client, query=query, index=original_index_name)
    number_of_records = es_client.count(index=original_index_name, body=query)["count"]
    haystack_documents: List[Dict] = []
    for idx, record in enumerate(tqdm(records, total=number_of_records, desc="Converting ES Records")):
        # Write batch_size number of documents to haystack DocumentStore
        if (idx + 1) % batch_size == 0:
            document_store.write_documents(haystack_documents, index=index)
            haystack_documents = []

        # Get content and metadata of current record
        content = record["_source"].pop(original_content_field, "")
        if content:
            record_doc = {"content": content, "meta": {}}

            if original_name_field is not None:
                if original_name_field in record["_source"]:
                    record_doc["meta"]["name"] = record["_source"].pop(original_name_field)
            # Only add selected metadata fields
            if included_metadata_fields is not None:
                for metadata_field in included_metadata_fields:
                    if metadata_field in record["_source"]:
                        record_doc["meta"][metadata_field] = record["_source"][metadata_field]
            # Add all metadata fields except for those in excluded_metadata_fields
            else:
                if excluded_metadata_fields is not None:
                    for metadata_field in excluded_metadata_fields:
                        record["_source"].pop(metadata_field, None)
                record_doc["meta"].update(record["_source"])

            if store_original_ids:
                record_doc["meta"]["_original_es_id"] = record["_id"]

            # Apply preprocessor if provided
            preprocessed_docs = preprocessor.process(record_doc) if preprocessor is not None else [record_doc]

            haystack_documents.extend(preprocessed_docs)

    if haystack_documents:
        document_store.write_documents(haystack_documents, index=index)

    return document_store
