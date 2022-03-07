import { useMemo } from 'react';
import { useTranslation } from 'react-i18next';
import { Column } from 'react-table';

import DataTable from '../../components/DataTable/DataTable';
import Layout from '../../components/Layout/Layout';
import { usePaginationAPI } from '../../hooks/api';
import * as schemas from '../../schemas';

const Clients: React.FunctionComponent = () => {
  const { t } = useTranslation(['clients']);
  const {
    data: clients,
    count,
    page,
    maxPage,
    onPageChange,
    sorting,
    onSortingChange,
  } = usePaginationAPI<'listClients'>({ method: 'listClients', limit: 10 });

  const columns = useMemo<Column<schemas.client.Client>[]>(() => {
    return [
      {
        Header: t('clients:list.name') as string,
        accessor: 'name',
        Cell: ({ cell: { value }, row: { original } }) => (
          <>
            {value}
            {original.first_party &&
              <div className="inline-flex font-medium rounded-full text-center ml-2 px-2.5 py-0.5 bg-green-100 text-green-600">
                {t('clients:list.first_party')}
              </div>
            }
          </>
        )
      },
      {
        Header: t('clients:list.tenant') as string,
        accessor: 'tenant',
        Cell: ({ cell: { value: tenant }}) => (
          <>{tenant.name}</>
        ),
      },
      {
        Header: t('clients:list.client_id') as string,
        accessor: 'client_id',
      },
    ];
  }, [t]);

  return (
    <Layout>
      <div className="sm:flex sm:justify-between sm:items-center mb-8">

        <div className="mb-4 sm:mb-0">
          <h1 className="text-2xl md:text-3xl text-slate-800 font-bold">{t('clients:list.title')}</h1>
        </div>

      </div>

      <DataTable
        title={t('clients:list.title')}
        count={count}
        pageSize={10}
        data={clients}
        columns={columns}
        sorting={sorting}
        onSortingChange={onSortingChange}
        page={page}
        maxPage={maxPage}
        onPageChange={onPageChange}
      />
    </Layout>
  );
};

export default Clients;
