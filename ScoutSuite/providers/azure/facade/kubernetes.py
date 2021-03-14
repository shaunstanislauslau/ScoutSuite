from azure.mgmt.hybridkubernetes import ConnectedKubernetesClient
from azure.mgmt.kubernetesconfiguration import SourceControlConfigurationClient

from ScoutSuite.core.console import print_exception
from ScoutSuite.providers.utils import run_concurrently
from ScoutSuite.utils import get_user_agent


class KubernetesFacade:

    def __init__(self, credentials):
        self.credentials = credentials

    def get_client(self, subscription_id: str):

        client = ConnectedKubernetesClient(self.credentials.get_credentials(),
                                           subscription_id,
                                           user_agent=get_user_agent())
        return client

    # def get_client2(self, subscription_id: str):
    #
    #     client = SourceControlConfigurationClient(self.credentials.get_credentials(),
    #                                        subscription_id,
    #                                        user_agent=get_user_agent())
    #     return client

    async def get_kubernetes_services(self, subscription_id: str):
        try:
            client = self.get_client(subscription_id)
            return await run_concurrently(
                lambda: list(client.connected_cluster.list_by_subscription())
            )
        except Exception as e:
            print_exception(f'Failed to retrieve Kubernetes Services: {e}')
            return []
    # async def get_kubernetes_config(self, subscription_id: str):
    #     try:
    #         client = self.get_client2(subscription_id)
    #         return await run_concurrently(
    #             lambda: list(client.source_control_configurations.)
    #         )
    #     except Exception as e:
    #         print_exception(f'Failed to retrieve Kubernetes Services: {e}')
    #         return []

    # async def get_instance_extensions(self, subscription_id: str,
    #                                   instance_name: str,
    #                                   resource_group: str):
    #     try:
    #         client = self.get_client(subscription_id)
    #         extensions = await run_concurrently(
    #             lambda: client.virtual_machine_extensions.list(resource_group,
    #                                                            instance_name)
    #         )
    #         return list(extensions.value)
    #     except Exception as e:
    #         print_exception(f'Failed to retrieve virtual machine extensions: {e}')
    #         return []
    #
    # async def get_disks(self, subscription_id: str):
    #     try:
    #         client = self.get_client(subscription_id)
    #         return await run_concurrently(
    #             lambda: list(client.disks.list())
    #         )
    #     except Exception as e:
    #         print_exception(f'Failed to retrieve disks: {e}')
    #         return []
    #
    # async def get_snapshots(self, subscription_id: str):
    #     try:
    #         client = self.get_client(subscription_id)
    #         return await run_concurrently(
    #             lambda: list(client.snapshots.list())
    #         )
    #     except Exception as e:
    #         print_exception(f'Failed to retrieve snapshots: {e}')
    #         return []
    #
    # async def get_images(self, subscription_id: str):
    #     try:
    #         client = self.get_client(subscription_id)
    #         return await run_concurrently(
    #             lambda: list(client.images.list())
    #         )
    #     except Exception as e:
    #         print_exception(f'Failed to retrieve images: {e}')
    #         return []
