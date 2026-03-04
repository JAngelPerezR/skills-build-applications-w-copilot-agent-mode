import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  useEffect(() => {
    const endpoint = `${process.env.REACT_APP_CODESPACE_URL}/api/users/`;
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Users endpoint:', endpoint);
        console.log('Fetched users:', data);
        setUsers(data.results || data);
      });
  }, []);
  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title">Users</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead className="table-dark">
              <tr>
                <th>Username</th>
                <th>Email</th>
                <th>Joined</th>
              </tr>
            </thead>
            <tbody>
              {users.map((user, idx) => (
                <tr key={idx}>
                  <td>{user.username || '-'}</td>
                  <td>{user.email || '-'}</td>
                  <td>{user.joined || '-'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
export default Users;
